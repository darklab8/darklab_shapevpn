from . import interface, ui


def test_interface() -> None:
    print(interface.parse([ui.Command.install.value]))
