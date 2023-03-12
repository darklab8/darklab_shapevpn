import logging
import re
from typing import Any, Dict, Generator, Protocol, cast

import docker  # type: ignore[import]
from celery import Task, shared_task

from backend_api.src import exceptions
from backend_api.src.core import settings as conf
from server_installer.src.interface import ui
from server_installer.src.storage.config_encryptor import ConfigEncryptor

from . import measurer

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
        task_id: str,
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

            self._task.update_state(
                state="PROGRESS",
                meta={
                    "current_number": self._task_counter,
                    "total": conf.INSTALLER_MAX_TASKS,
                    "current_name": task_record.group(1),
                },
            )


class InstallServerTask:
    extra_container_run_args: dict[str, Any] = {}

    def __init__(
        self,
        task: Task,
        start_time: str,
        unique_id: str,
        task_id: str,
        user_input: ui.UserInput,
    ):
        self._task = task
        self._start_time = start_time
        self._unique_id = unique_id
        self._task_id = task_id
        self._user_input = user_input

        self._client = docker.from_env()
        self._environments = dict(task_id=self._task_id)

    def _setup(self) -> None:
        logging.info(f"unique_id={self._unique_id}, running containers.run")

        self._user_input.redis_host = conf.REDIS_RESULT_HOST
        self._user_input.redis_pass = conf.REDIS_RESULT_PASSWORD
        self._user_input.redis_port = conf.REDIS_RESULT_PORT

    def _launch(self) -> Container:
        container = self._client.containers.run(
            conf.INSTALLER_IMAGE,
            environment=self._environments,
            detach=True,
            command=self._user_input.install_args(),
            **self.extra_container_run_args,
            network_mode="host",
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


@shared_task(bind=True)
def task_vpn_install(
    self: Task, user_input: Dict[str, Any], unique_id: str = "undefined"
) -> str:
    logging.info(f"unique_id={unique_id}, task_vpn_install begins")
    start_time = measurer.start_time_measuring()
    task_id = self.request.id

    InstallServerTask(
        task=self,
        start_time=start_time,
        unique_id=unique_id,
        task_id=task_id,
        user_input=ProtectedSerializer.deserialize(**user_input),
    ).run()
    return f"succesful_installation_{unique_id}"
