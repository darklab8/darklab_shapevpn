import json
from enum import Enum
from typing import Dict, List

from pydantic import BaseModel


class Command(str, Enum):
    install = "install"
    test_install = "test_install"
    enable_password_login = "enable_password_login"  # refactor if u need
    change_ssh_port_to_22000 = "change_ssh_port_to_22000"  # refactor if u need


class AuthType(str, Enum):
    ssh = "ssh"
    password = "password"


class RedisInput(BaseModel):
    redis_host: str = ""
    redis_port: int = 6379
    redis_pass: str = ""
    task_id: str = ""
    encryption_key: str = ""


class AuthInput(BaseModel):
    auth_type: AuthType = AuthType.ssh
    ip: str = ""
    password: str = ""
    user: str = ""
    server_ssh_port: int = 22
    private_key: str = ""


class WireguardInput(BaseModel):
    users_amount: int = 5
    server_vpn_port: int = 31280


class UserInput(RedisInput, AuthInput, WireguardInput):
    command: Command = Command.install

    def to_args(self) -> List[str]:
        arguments: Dict[str, str] = json.loads(self.json())
        arguments.pop("command")
        args = []
        for key, value in arguments.items():
            args.append(f"--{key}")
            args.append(str(value))
        return args
