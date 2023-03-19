import logging
from pathlib import Path
from typing import Optional, Sequence

from . import exceptions
from .ansible import playbooks
from .ansible.configs import verify_configs_existence
from .ansible.create_hosts_file import create_hosts_file
from .ansible.jsonify import get_json_of_configs
from .interface import interface, ui
from .storage import redis
from .utils import logger

configs_folder = Path("configs")


def installing_vpn(query: ui.UserInput) -> None:
    redis_conn = redis.RedisInstaller(
        redis_host=query.redis_host,
        redis_port=query.redis_port,
        redis_pass=query.redis_pass,
        task_id=query.task_id,
    )
    if redis_conn.active:
        logging.info(
            f"task_id={query.task_id}, msg=redis_is_active, content=installing_beginning"
        )

    create_hosts_file(query=query)

    logging.info(f"task_id={query.task_id}, type=install_vpn, msg=start")
    result = playbooks.install_vpn(query=query)

    if result.returncode != 0:
        logging.warn(
            f"task_id={query.task_id}, type=install_vpn, msg=retrying_installation"
        )
        result = playbooks.install_vpn(query=query)

    if redis_conn.active:
        logging.info(
            f"task_id={query.task_id}, msg=saving_to_redis content=result.stdout"
        )
        redis_conn.set_stdout(data=result.stdout)

    if not verify_configs_existence(configs_folder):
        logging.info(f"task_id={query.task_id}, msg=configs were not found")
        raise exceptions.NotFound("configs were not found")

    logging.info(f"task_id={query.task_id}, type=get_json_of_configs")
    configs_data = get_json_of_configs(configs_folder)

    if redis_conn.active:
        logging.info(f"task_id={query.task_id}, msg=saving_to_redis content=configs")

        redis_conn.set_config(
            data=configs_data, configs_encryption_key=query.configs_encryption_key
        )
        logging.info(
            f"task_id={query.task_id}, msg=redis_is_active, content=succesful_installation"
        )


def test_installing_vpn(query: ui.UserInput) -> None:
    redis_conn = redis.RedisInstaller(
        redis_host=query.redis_host,
        redis_port=query.redis_port,
        redis_pass=query.redis_pass,
        task_id=query.task_id,
    )
    if redis_conn.active:
        logging.info(
            f"task_id={query.task_id}, msg=redis_is_active, content=installing_beginning"
        )

    create_hosts_file(query=query)

    logging.info(f"task_id={query.task_id}, type=install_vpn, msg=start")
    result = playbooks.Result(stdout="123", returncode=0)

    if redis_conn.active:
        logging.info(
            f"task_id={query.task_id}, msg=saving_to_redis content=result.stdout"
        )
        redis_conn.set_stdout(data=result.stdout)

    configs_folder = Path(__file__).parent / "ansible" / "testdata" / "configs"
    if not verify_configs_existence(configs_folder):
        logging.info(f"task_id={query.task_id}, msg=configs were not found")
        raise exceptions.NotFound("configs were not found")

    logging.info(f"task_id={query.task_id}, type=get_json_of_configs")
    configs_data = get_json_of_configs(configs_folder)

    if redis_conn.active:
        logging.info(f"task_id={query.task_id}, msg=saving_to_redis content=configs")

        redis_conn.set_config(
            data=configs_data, configs_encryption_key=query.configs_encryption_key
        )
        logging.info(
            f"task_id={query.task_id}, msg=redis_is_active, content=succesful_installation"
        )


def allow_password_access(query: ui.UserInput) -> None:
    logging.info(
        f"task_id={query.task_id}, msg=allow_password_access creating host file"
    )
    create_hosts_file(query=query)
    logging.info(f"msg=allow_password_access processing")
    playbooks.allow_password_access()


def change_ssh_port(query: ui.UserInput) -> None:
    logging.info(
        f"task_id={query.task_id}, msg=allow_password_access creating host file"
    )
    create_hosts_file(query=query)
    logging.info(f"msg=change_ssh_port processing")
    playbooks.change_ssh_port()


def main(args: Optional[Sequence[str]] = None) -> None:
    logger.configure()
    logging.debug("launching server_installer")
    query = interface.parse(args=args)

    if query.command == ui.Command.install:
        installing_vpn(query=query)
    elif query.command == ui.Command.test_install:
        test_installing_vpn(query=query)
    elif query.command == ui.Command.enable_password_login:
        allow_password_access(query=query)
    elif query.command == ui.Command.change_ssh_port_to_22000:
        change_ssh_port(query=query)
