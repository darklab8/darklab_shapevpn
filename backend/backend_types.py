from enum import Enum
from typing import NewType

from pydantic import BaseModel
from typing_extensions import Self

TaskID = NewType("TaskID", str)


class Message(str, Enum):
    ping = "ping"


class PingResponce(BaseModel):
    message: Message

    @classmethod
    def ping(cls) -> Self:
        return cls(message=Message.ping)
