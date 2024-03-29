import logging
import os
import re
import secrets
from typing import Any, Dict, Generator, Protocol, cast

import docker  # type: ignore[import]
from celery import Task, shared_task

from backend_api_OLD.src import exceptions
from backend_api_OLD.src.core import settings as conf
from backend_api_OLD.src.types import TaskID
from server_installer.src.interface import ui
from server_installer.src.storage.config_encryptor import ConfigEncryptor

from . import measurer, status

secret_encryptor = ConfigEncryptor(conf.REDIS_SECRET_KEY)


class TaskStatus:
    PENDING = "PENDING"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"


class ProtectedSerializer:
    @classmethod
    def serialize(cls, instance: ui.UserInput) -> Dict[str, Any]:
        instance.password = secret_encryptor.encrypt_str(instance.password)
        instance.private_key = secret_encryptor.encrypt_str(instance.private_key)
        instance.configs_encryption_key = secret_encryptor.encrypt_str(
            instance.configs_encryption_key
        )

        return instance.dict()

    @classmethod
    def deserialize(cls, **data: Dict[str, Any]) -> ui.UserInput:
        instance = ui.UserInput(**data)
        instance.password = secret_encryptor.decrypt_str(instance.password)
        instance.private_key = secret_encryptor.decrypt_str(instance.private_key)
        instance.configs_encryption_key = secret_encryptor.decrypt_str(
            instance.configs_encryption_key
        )
        return instance


class ContainerLogs(Protocol):
    def __iter__(self) -> Generator[bytes, None, None]:
        ...


class Container(Protocol):
    def logs(self, stream: bool) -> ContainerLogs:
        ...


class ContainerLogHandler:
    def __init__(
        self,
        log_stream: ContainerLogs,
        task_id: TaskID,
        task: Task,
    ):
        self._log_stream = log_stream
        self._task_id = task_id
        self._task = task

        self._succesful_installlation = False
        self._task_counter = 0
        self._is_unrechable_error_two_times = 0

        self._success_msg = "content=succesful_installation"
        self._server_unrechable_msg = "UNREACHABLE! => "

    def run(self) -> None:
        for log_record in self._log_stream:
            decoded_log_string = log_record.decode("utf-8")
            print(f"{decoded_log_string=}")
            if decoded_log_string == "\n":
                continue

            if self._success_msg in decoded_log_string:
                self._succesful_installlation = True

            if self._server_unrechable_msg in decoded_log_string:
                self._is_unrechable_error_two_times += 1

            logging.info(
                f"task_id={self._task_id}, type=containers.run, stdout={decoded_log_string}"
            )

            task_record = re.search("=TASK \[(.+)\].[*]+", decoded_log_string)
            if task_record is None:
                continue

            self._task_counter += 1

            redis_conn = status.RedisBackend.create(self._task_id)

            redis_conn.set_status(
                status.StatusData(
                    state=status.StatusState.PROGRESS,
                    current_number=self._task_counter,
                    current_name=task_record.group(1),
                )
            )


class InstallServerTask:
    def __init__(
        self,
        task: Task,
        start_time: str,
        unique_id: str,
        task_id: TaskID,
        user_input: ui.UserInput,
        installer_image: str,
    ):
        self._task = task
        self._start_time = start_time
        self._unique_id = unique_id
        self._task_id = task_id
        self._user_input = user_input

        self._client = docker.from_env()
        self._environments = dict(task_id=self._task_id)
        self._installer_image = installer_image

    def _setup(self) -> None:
        logging.info(f"unique_id={self._unique_id}, running containers.run")

        self._user_input.redis_host = conf.REDIS_RESULT_HOST
        self._user_input.redis_pass = conf.REDIS_RESULT_PASSWORD
        self._user_input.redis_port = conf.REDIS_RESULT_PORT

    def _launch(self) -> Container:
        container = self._client.containers.run(
            self._installer_image,
            environment=self._environments,
            detach=True,
            command=self._user_input.install_args(),
            **conf.network_args,
        )

        assert container is not None
        return cast(Container, container)

    def run(self) -> None:
        self._setup()

        try:
            container = self._launch()
            log_stream = container.logs(stream=True)

            logs = ContainerLogHandler(
                log_stream,
                task_id=self._task_id,
                task=self._task,
            )
            logs.run()

            if logs._is_unrechable_error_two_times >= 2:
                raise exceptions.UnreachableException("failed_installation")

            if not logs._succesful_installlation:
                raise exceptions.JobHandlerException(
                    "failed_installation. succesful_installation msg is not detected."
                )

        except docker.errors.ContainerError as stderr:
            logging.error(
                f"task_id={self._task_id}, type=containers.run, stderr={stderr}"
            )
            raise docker.errors.ContainerError("docker_error") from stderr
        finally:
            logging.info(
                f"task_id={self._task_id}, type=task_vpn_install, total_seconds={measurer.get_total_time_measuring(self._start_time)}"
            )


import time


@shared_task(bind=True)
def debug_my_task(self: Task) -> str:
    print("TASK: starting task")
    task_id = self.request.id
    redis_conn = status.RedisBackend.create(TaskID(task_id))
    redis_conn.set_status(
        status.StatusData(
            state=status.StatusState.PROGRESS,
        )
    )
    print("TASK: updating task state")
    time.sleep(2)
    print("TASK: finish sleaping")
    return task_id
