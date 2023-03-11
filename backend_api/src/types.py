from enum import Enum

from pydantic import BaseModel
from typing_extensions import Self


class Message(str, Enum):
    ping = "ping"


class PingResponce(BaseModel):
    message: Message

    @classmethod
    def ping(cls) -> Self:
        return cls(message=Message.ping)
