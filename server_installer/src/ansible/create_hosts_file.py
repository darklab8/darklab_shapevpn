from jinja2 import Template
import logging
from . import ssh
from pathlib import Path
from ..interface import ui
from .. import exceptions


def create_hosts_file(
    query: ui.UserInput,
) -> None:
    logging.info(f"task_id={query.task_id}, type=PRIVATE_KEY_COPYING")
    ssh.write_to_file(query.private_key)

    if not query.ip:
        raise exceptions.NotFound("The terror! ip_address is not defined.")

    if not query.user:
        raise exceptions.NotFound("The terror! user is not defined.")

    if not query.users_amount:
        raise exceptions.NotFound("The terror! users_amount is not defined.")

    logging.info(f"task_id={query.task_id}, reading ip address = {query.ip} from env")

    with open(str(Path(__file__).parent / "files" / "hosts.yml.jinja2"), "r") as file_:
        template_content = file_.read()

    to_render = {
        "server_vpn_port": query.server_vpn_port,
        "server_ssh_port": query.server_ssh_port,
        "server_target": query.ip,
        "user": query.user,
        "users": query.users_amount,
    }

    if query.auth_type == ui.AuthType.ssh:
        to_render.update({})

    if query.auth_type == ui.AuthType.password:
        if not query.password:
            raise exceptions.NotFound("password is not defined, but auth type is pass")

        if not query.user:
            raise exceptions.NotFound("user is not defined, can't install vpn")

        to_render.update({"password": query.password})

    logging.info(
        f"task_id={query.task_id}, type=creating host file, content={to_render.keys()}"
    )

    with open("hosts.yml", "w") as file_:
        t = Template(template_content)
        rendered = t.render(**to_render)
        file_.write(rendered)

    with open("hosts2.yml", "w") as file_:
        t = Template(template_content)
        to_render["is_docker_py"] = True
        rendered = t.render(**to_render)
        file_.write(rendered)

    logging.info(f"task_id={query.task_id}, hosts file is rendered")
