import json
import logging
import secrets
from typing import Optional, TypedDict

from celery.result import AsyncResult
from fastapi import APIRouter, Body
from pydantic import BaseModel

from backend_api.src.core import settings
from backend_api.src.core.celery import app as celery_app
from backend_api.src.core.celery import task_vpn_install
from server_installer.src.interface.ui import AuthType, UserInput
from server_installer.src.storage import redis
from server_installer.src.storage.config_encryptor import ConfigEncryptor
from server_installer.src.supported_oses import SupportedOSes

from ..types import PingResponce
from .code.encryption import AssymetricEncryptor
from .tasks import ProtectedSerializer

router_example = APIRouter(
    prefix="/ping",
    tags=["ping"],
)


@router_example.get(path="/")
async def ping_get() -> PingResponce:
    return PingResponce.ping()


@router_example.post(path="/")
async def ping_post() -> PingResponce:
    return PingResponce.ping()


router_install = APIRouter(
    prefix="/task",
    tags=["install"],
)


class GeneratedKeys(BaseModel):
    private: str
    public: str
    data_key: str


@router_install.get(path="/keys")
async def generate_keys() -> GeneratedKeys:
    private, public = AssymetricEncryptor.generate_keys()
    data_key = ConfigEncryptor.generate_key()
    return GeneratedKeys(
        private=private,
        public=public,
        data_key=data_key,
    )


class InstallingData(BaseModel):
    auth: AuthType = AuthType.ssh
    ip_address: str
    data_key: str

    user: str = "root"
    server_ssh_port: int = 22
    server_vpn_port: int = 31280

    ssh_key: Optional[str]
    password: Optional[str]


InstallResponse = TypedDict("InstallResponse", {"task_id": str})


@router_install.post(
    path="/",
    summary="Install Wireguard to your server",
    description=f""".\n
    hint #1: supports ssh and password authentification methods\n
    hint #2: get data_key from Generate Keys request.\n
    hint #3: supported target server OSes: {SupportedOSes.list()}""",
)
def install_vpn_server(
    installing: InstallingData = Body(
        embed=False,
        title="12",
        description="34",
        examples={
            "example_with_ssh": dict(
                summary="example with ssh",
                value=InstallingData(
                    auth=AuthType.ssh,
                    ip_address="217.36.76.12",
                    data_key="key from /keys['data_key']",
                    user="root",
                    ssh_key="ssh key",
                ).dict(),
            ),
            "example_with_password": dict(
                summary="example with password",
                value=InstallingData(
                    auth=AuthType.password,
                    ip_address="217.36.76.23",
                    data_key="key from /keys['data_key']",
                    user="root",
                    password="my password",
                ).dict(),
            ),
        },
    ),
) -> InstallResponse:
    unique_id = secrets.token_hex(16)
    logging.info(f"unique_id={unique_id}, type=install_vpn_server, msg=start")

    logging.info(
        f"unique_id={unique_id}, type=install_vpn_server, msg=start, {installing=}"
    )  # debug

    task = task_vpn_install.delay(
        unique_id=unique_id,
        user_input=ProtectedSerializer.serialize(
            UserInput(
                auth_type=installing.auth,
                ip=installing.ip_address,
                user=installing.user,
                server_ssh_port=installing.server_ssh_port,
                server_vpn_port=installing.server_vpn_port,
                configs_encryption_key=installing.data_key,
                private_key=installing.ssh_key,
                password=installing.password,
            )
        ),
    )
    logging.info(
        f"unique_id={unique_id}, type=install_vpn_server, msg=finish, status_code=200, task_id={task.id}"
    )
    return {"task_id": "task.id"}


StatusResponse = TypedDict("StatusResponse", {"task_id": str, "meta": dict})


@router_install.get(path="/{task_id}")
def get_status(task_id: str) -> StatusResponse:
    task: AsyncResult = AsyncResult(task_id, app=celery_app)

    print(f"meta={task.info}")

    try:
        json.dumps(task.info)
        meta = task.info
    except (TypeError, OverflowError):
        meta = {}

    if meta is None:
        meta = {}

    return {"task_id": task.status, "meta": meta}


StdoutResponse = TypedDict("StdoutResponse", {"stdout": str})


@router_install.get(path="/{task_id}/stdout")
def get_stdout(task_id: str) -> StdoutResponse:
    redis_conn = redis.Redis(
        redis_host=settings.REDIS_RESULT_HOST,
        redis_port=settings.REDIS_RESULT_PORT,
        redis_pass=settings.REDIS_RESULT_PASSWORD,
        task_id=task_id,
    )

    # TODO type it
    data = redis_conn.get_stdout()
    if data is None:
        return {"stdout": "not found"}
    return {"stdout": data}


ConfigResponse = TypedDict("ConfigResponse", {"configs": str})


@router_install.get(path="/{task_id}/configs")
def get_configs(task_id: str, data_key: str) -> ConfigResponse:
    redis_conn = redis.Redis(
        redis_host=settings.REDIS_RESULT_HOST,
        redis_port=settings.REDIS_RESULT_PORT,
        redis_pass=settings.REDIS_RESULT_PASSWORD,
        task_id=task_id,
    )

    decrypted = redis_conn.get_config(data_key)

    assert decrypted is not None

    return {"configs": decrypted}
