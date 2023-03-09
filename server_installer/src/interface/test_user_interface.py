from . import interface
from . import ui


def test_interface() -> None:
    print(interface.parse([ui.Command.install.value]))
