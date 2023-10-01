from pydantic import BaseModel
from typing import NewType

ServerPort = NewType("ServerPort", int)
SSHPrivateKeyPath = NewType("SSHPrivateKeyPath", str)
ServerHostname = NewType("ServerHostname", str)

class InputData(BaseModel):
    port: ServerPort = ServerPort(22)
    key: SSHPrivateKeyPath
    hostname: ServerHostname

class Installer:
    def __init__(self, data: InputData):
        self._data = data

    def run(self) -> None:
        pass
