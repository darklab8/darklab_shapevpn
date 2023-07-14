from enum import Enum


class SupportedOSes(str, Enum):
    ubuntu2004 = "ubuntu 20.04"

    @classmethod
    def list(cls) -> str:
        return ", ".join([e.value for e in cls])
