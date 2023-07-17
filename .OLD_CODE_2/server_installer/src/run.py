from .interface import interface, ui
from .utils import logger
from .app import installing_vpn, test_installing_vpn, allow_password_access, change_ssh_port
from typing import Optional, Sequence
import logging

def run_query(query: interface.UserInput):
    logger.configure()
    logging.debug("launching run_query")

    if query.command == ui.Command.install:
        installing_vpn(query=query)
    elif query.command == ui.Command.test_install:
        test_installing_vpn(query=query)
    elif query.command == ui.Command.enable_password_login:
        allow_password_access(query=query)
    elif query.command == ui.Command.change_ssh_port_to_22000:
        change_ssh_port(query=query)

def run_with_args(args: Optional[Sequence[str]] = None) -> None:
    query = interface.parse(args=args)
    run_query(query)