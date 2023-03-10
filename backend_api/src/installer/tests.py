import time
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from backend_api.src.core import settings as conf
from backend_api.src.core.celery import task_vpn_install
from backend_api.src.types import PingResponce
from server_installer.src.interface import ui
from server_installer.src.utils import logger

from . import measurer, tasks


@pytest.mark.asyncio
async def test_ping_example(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == PingResponce.ping()


def test_vpn_install_directly(installer_image: str) -> None:
    ui.install_command = ui.Command.test_install
    conf.INSTALLER_IMAGE = installer_image

    logger.configure()
    task = MagicMock()
    tasks.InstallServerTask(
        task_id="123",
        task=task,
        unique_id="undefined",
        start_time=measurer.start_time_measuring(),
        user_input=ui.UserInput(
            auth_type=ui.AuthType.ssh,
            ip="123.123.123.123",
            private_key="123",
            password="456",
            configs_encryption_key="1InvkFDBGKDLpawxL6U2r0O4aVZJbPJI-XPwy7GudSs=",
            user="root",
            task_id="defined_to_trigger_recording_to_redis",
        ),
    ).run()


def test_vpn_install_task(
    celery_app: None, celery_worker: None, installer_image: str
) -> None:
    ui.install_command = ui.Command.test_install
    conf.INSTALLER_IMAGE = installer_image

    logger.configure()
    task_vpn_install.delay(
        tasks.ProtectedSerializer.serialize(
            ui.UserInput(
                auth_type=ui.AuthType.ssh,
                ip="123.123.123.123",
                private_key="123",
                password="456",
                configs_encryption_key="1InvkFDBGKDLpawxL6U2r0O4aVZJbPJI-XPwy7GudSs=",
                user="root",
                task_id="defined_to_trigger_recording_to_redis",
            )
        ),
    ).get(timeout=30)


from celery.result import AsyncResult


def test_check_task_status(celery_app: None, celery_worker: None) -> None:
    print("starting task")
    task = tasks.debug_my_task.delay()
    # task.get(timeout=30)
    print("the task is sent")
    print(f"{task.id}")

    for _ in range(5):
        state = AsyncResult(task.id).status
        print(f"{state=}")
        if state == "PROGRESS":
            break
        time.sleep(1)
    else:
        assert False, "progress state is not found"
