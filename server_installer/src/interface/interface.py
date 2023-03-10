import argparse
from typing import Sequence, Optional
import logging
from .ui import UserInput, Command, RedisInput, AuthInput, WireguardInput


def parse(args: Optional[Sequence[str]] = None) -> UserInput:
    parser = argparse.ArgumentParser(
        prog="Server installer",
        description="""
                    it installs wireguard to server.
                    Currently supports ubuntu 20.04 at Hetzner and Vultr cloud providers
                    """,
    )

    subparsers = parser.add_subparsers(
        required=True,
        dest="command",
    )

    install = subparsers.add_parser(Command.install.name)
    install_args(install)

    test_install = subparsers.add_parser(Command.install.test_install)
    install_args(test_install)

    parsed = parser.parse_args(args)
    query = UserInput(
        **{key: value for key, value in parsed.__dict__.items() if value is not None}
    )
    return query

def install_args(install: argparse.ArgumentParser) -> None:
    redis = install.add_argument_group("redis")
    redis.add_argument(
        "--redis_host",
        type=RedisInput.__annotations__["redis_host"],
        default=None,
    )
    redis.add_argument(
        "--redis_port",
        type=RedisInput.__annotations__["redis_port"],
        default=None,
    )
    redis.add_argument(
        "--redis_pass",
        type=RedisInput.__annotations__["redis_pass"],
        default=None,
    )
    redis.add_argument(
        "--task_id",
        type=RedisInput.__annotations__["task_id"],
        default=None,
    )
    redis.add_argument(
        "--encryption_key",
        type=RedisInput.__annotations__["encryption_key"],
        default=None,
    )

    auth = install.add_argument_group("auth")
    auth.add_argument(
        "--auth_type",
        type=AuthInput.__annotations__["auth_type"],
        default=None,
    )
    auth.add_argument(
        "--ip",
        type=AuthInput.__annotations__["ip"],
        default=None,
    )
    auth.add_argument(
        "--password",
        type=AuthInput.__annotations__["password"],
        default=None,
    )
    auth.add_argument(
        "--user",
        type=AuthInput.__annotations__["user"],
        default=None,
    )
    auth.add_argument(
        "--private_key",
        type=AuthInput.__annotations__["private_key"],
        default=None,
    )
    auth.add_argument(
        "--server_ssh_port",
        type=AuthInput.__annotations__["server_ssh_port"],
        default=None,
    )

    wireguard = install.add_argument_group("wireguard")
    wireguard.add_argument(
        "--users_amount",
        type=WireguardInput.__annotations__["users_amount"],
        default=None,
    )
    wireguard.add_argument(
        "--server_vpn_port",
        type=WireguardInput.__annotations__["server_vpn_port"],
        default=None,
    )
