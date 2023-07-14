import os

from celery import Celery
import time
import secrets
import subprocess
import sys
import redis
import base64
import json
import docker
import re

# from .settings import CELERY_CACHE_BACKEND

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from dotenv import load_dotenv
from pathlib import Path
import secrets
import contextlib
import core.measurer as measurer
from . import exceptions as exceptions

import logging
logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

from . import shared_settings as shared_settings
from .encryptor import secret_encryptor

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

REDIS_QUEUE_PASSWORD = os.environ["redis_queue_password"]
REDIS_RESULT_PASSWORD = os.environ["redis_result_password"]
REDIS_HOST_QUEUE = os.environ["queue"]
REDIS_HOST_RESULT = os.environ["result"]
image = os.environ.get(
    "image",
    "registry.gitlab.com/gtn_admins/constructor/constructor_server_installer/constructor-installer:latest",
)
# celery setting.
CELERY_CACHE_BACKEND = f"redis://:{REDIS_QUEUE_PASSWORD}@{REDIS_HOST_QUEUE}:{shared_settings.REDIS_QUEUE_PORT}/0"  # 'default'


app = Celery("core", broker=CELERY_CACHE_BACKEND)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
REDIS_RESULT_FULL_ADDRESS = f"redis://:{REDIS_RESULT_PASSWORD}@{REDIS_HOST_RESULT}:{shared_settings.REDIS_RESULT_PORT}/0"
print(REDIS_RESULT_FULL_ADDRESS)
app.conf.result_backend = REDIS_RESULT_FULL_ADDRESS
# app.conf.task_track
# Load task modules from all registered Django apps.
app.autodiscover_tasks()


class TaskStatus:
    PENDING = "PENDING"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"


# custom redis
redis_conn = redis.Redis(host=REDIS_HOST_RESULT, password=REDIS_RESULT_PASSWORD, port=int(shared_settings.REDIS_RESULT_PORT), db=0)


@app.task(bind=True)
def debug_task(self):
    print("starting task")

    time.sleep(1)
    self.update_state(state="PROGRESS")
    return "123"


@app.task(bind=True)
def debug_task_can_input_which_data(self, data):
    print(data)
    print("starting task")
    self.update_state(state="PROGRESS")
    return data


@app.task(bind=True)
def test_debug_docker(
    self, auth, ip_address=None, user="root", password="", api_key=""
):

    self.update_state(state="PROGRESS")

    result = subprocess.run(
        # [sys.executable, "-c", "print('ocean')"], capture_output=True, text=True
        [f"docker ps"],
        capture_output=True,
        shell=True,
        text=True,
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    return "123"


def turn_configs_to_dictionary(filepath):
    result = {}

    for root, subdirs, files in os.walk(filepath):
        for file in files:
            path = f"{root}/{file}"

            if ".conf" in file:
                with open(path, "rb") as file_:
                    encoded = base64.b64encode(file_.read()).decode("utf-8")
                    result[file] = encoded
                    # print(encoded)
                    # decoded = base64.b64decode(encoded.encode("utf-8"))
                    # print(decoded.decode("utf-8"))
            else:
                with open(path, "rb") as file_:
                    encoded = base64.b64encode(file_.read()).decode("utf-8")
                    result[file] = encoded
    return result


class RedisPipeline:
    def __init__(self):
        pass

    def __enter__(self):
        self.pipe = redis_conn.pipeline()
        return self.pipe

    def __exit__(self, type, value, traceback):
        self.pipe.execute()


@app.task(bind=True)
def task_get_id(self):
    print(self.request.id)


def launch_task_in_docker_image_to_install_vpnserver(
    ip_address,
    user,
    task_id,
    auth,
    password,
    task,
    start,
    server_ssh_port,
    server_vpn_port,
    private_key,
    data_key,
    unique_id,
):
    
    client = docker.from_env()
    environments = {
        "ip": ip_address,
        "user": user,
        "task_id": task_id,
        "auth": auth,
        "password": password,
        "redis_host": REDIS_HOST_RESULT,
        "redis_pass": REDIS_RESULT_PASSWORD,
        "redis_host_port": shared_settings.REDIS_RESULT_PORT,
        "server_ssh_port": server_ssh_port,
        "server_vpn_port": server_vpn_port,
        "private_key": private_key,
        "data_key": data_key
    }
    logging.info(f"unique_id={unique_id}, running containers.run for ip={ip_address}")

    try:
        container = client.containers.run(image, 
        environment=environments,
        detach=True
        )

        log_stream = container.logs(stream=True)

        task_counter = 0
        max_tasks = shared_settings.INSTALLER_MAX_TASKS
        succesful_installlation = False
        is_unrechable_error_two_times = 0
        for log_record in log_stream:
            decoded_log_string = log_record.decode("utf-8") 

            if decoded_log_string == '\n':
                continue

            if "content=succesful_installation" in decoded_log_string:
                succesful_installlation = True
            
            if "UNREACHABLE! => " in decoded_log_string:
               is_unrechable_error_two_times += 1 

            logging.info(f"task_id={task_id}, type=containers.run, stdout={decoded_log_string}")

            task_record = re.search('=TASK \[(.+)\].[*]+', decoded_log_string)
            if task_record is None:
                continue

            task_counter += 1

            task.update_state(state="PROGRESS", meta={'current_number': task_counter, 'total': max_tasks, 'current_name': task_record.group(1)})
        
        if is_unrechable_error_two_times >= 2:
            raise exceptions.ShapvpnInstallationUnreachableException("failed_installation")

        if not succesful_installlation:
            raise exceptions.ShapevpnInstallationGeneralException("failed_installation")

    except docker.errors.ContainerError as stderr:
        logging.error(f"task_id={task_id}, type=containers.run, stderr={stderr}")
        raise Exception("docker_error") from stderr

    finally:
        logging.info(f"task_id={task_id}, type=task_vpn_install, total_seconds={measurer.get_total_time_measuring(start)}")

@app.task(bind=True)
def task_vpn_install(
    self,
    auth,
    start,
    ip_address,
    private_key,
    data_key,
    unique_id,
    user="root",
    password="",
    server_ssh_port="22",
    server_vpn_port="31280",

):

    logging.info(f"unique_id={unique_id}, task_vpn_install begins")

    task_id = self.request.id

    launch_task_in_docker_image_to_install_vpnserver(
        auth=auth,
        ip_address=ip_address,
        task_id=task_id,
        user=user,
        password=secret_encryptor.decrypt_str(password),
        task=self,
        start=start,
        server_ssh_port=server_ssh_port,
        server_vpn_port=server_vpn_port,
        private_key=secret_encryptor.decrypt_str(private_key),
        data_key=secret_encryptor.decrypt_str(data_key),
        unique_id=unique_id,
    )
    return f"succesful_installation_{unique_id}"
