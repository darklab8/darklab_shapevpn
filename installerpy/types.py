from enum import Enum
from typing import NewType

from pydantic import BaseModel

ServerPort = NewType("ServerPort", int)
SSHPrivateKeyPath = NewType("SSHPrivateKeyPath", str)
ServerHostname = NewType("ServerHostname", str)

Command = NewType("Command", str)
TaskID = NewType("TaskID", str)
TaskName = NewType("TaskName", str)
LogLine = NewType("LogLine", str)


class RecordType(str, Enum):
    stdout = "stdout"
    stderr = "stderr"


class LogRecord(BaseModel):
    task_id: TaskID
    task_name: TaskName
    line: LogLine
    type: RecordType


RedisHost = NewType("RedisHost", str)
RedisPort = NewType("RedisPort", int)
