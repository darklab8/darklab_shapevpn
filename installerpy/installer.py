from pydantic import BaseModel

from . import types


class InputData(BaseModel):
    port: types.ServerPort = types.ServerPort(22)
    key: types.SSHPrivateKeyPath
    hostname: types.ServerHostname


class Installer:
    def __init__(self, data: InputData):
        self._data = data

    def run(self) -> None:
        pass
