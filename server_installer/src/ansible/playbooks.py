import logging
import os
import subprocess
from dataclasses import dataclass
from os.path import exists

from .. import exceptions
from ..interface import ui
from . import ssh


@dataclass
class Result:
    stdout: str
    returncode: int


def install_vpn(query: ui.UserInput) -> Result:
    if not exists("hosts.yml"):
        raise exceptions.NotFound("The terror!: hosts.yml is not found.")

    ansible_code_auth = ""
    if query.auth_type == ui.AuthType.ssh:
        ansible_code_auth = f'--key-file="{ssh.private_key_filename}"'

    log_records: list[str] = []
    proc = subprocess.Popen(
        f"ansible-playbook -i hosts.yml install_dockered_requirements.yml {ansible_code_auth}"
        + f" && ansible-playbook -i hosts2.yml install_dockered_wireguard.yml {ansible_code_auth}"
        + f" && ansible-playbook -i hosts.yml download_configs.yml {ansible_code_auth}",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )

    assert proc.stdout is not None

    for line in proc.stdout:
        line_str = line.decode("utf-8")
        logging.info(
            f"stdout, task_id={query.task_id}, type=install_vpn, stdout_line={line_str}"
        )
        log_records.append(line_str)
    proc.wait()

    if proc.stderr is not None:
        for line in proc.stderr:
            line_str = line.decode("utf-8")
            logging.info(
                f"stderr, task_id={query.task_id}, type=install_vpn, stdout_line={line_str}"
            )
            log_records.append(line_str)

    result = Result(stdout="".join(log_records), returncode=proc.returncode)
    return result


def allow_password_access() -> None:
    assert (
        os.system(
            f'ansible-playbook -i hosts.yml enable_password_login_for_test.yml --key-file="{ssh.private_key_filename}"'
        )
        == 0
    )


def change_ssh_port() -> None:
    assert (
        os.system(
            f'ansible-playbook -i hosts.yml change_ssh_port_to_22000_for_test.yml --key-file="{ssh.private_key_filename}"'
        )
        == 0
    )
