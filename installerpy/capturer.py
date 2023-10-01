"""
Captures shell output and puts to somewhere
"""
import subprocess
from typing import NewType, Protocol
from enum import Enum
from typing_extensions import Self
from pydantic import BaseModel

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

class Observer(Protocol):
    def notify(self, task_Id: TaskID, log_records: list[LogRecord]) -> None: ...

class Capturer:
    def __init__(
            self,
            cmd: Command,
            task_id: TaskID,
            task_name: TaskName,
        ):
        self._cmd = cmd
        self._task_id = task_id
        self._task_name = task_name
        self._observers: list[Observer] = []
        self._log_records: list[LogRecord] = []

    def register_observer(self, observer: Observer) -> Self:
        self._observers.append(observer)
        return self

    def _notify_observers(self) -> None:
        for observer in self._observers:
            observer.notify(self._task_id, self._log_records)

    def run(self) -> None:
        proc = subprocess.Popen(
            self._cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
        )

        assert proc.stdout is not None

        for line in proc.stdout:
            line_str = LogLine(line.decode("utf-8"))
            record = LogRecord(
                type=RecordType.stdout,
                task_id=self._task_id,
                task_name=self._task_name,
                line=line_str,
            )
            self._log_records.append(record)
            self._notify_observers()

        proc.wait()

        if proc.stderr is not None:
            for line in proc.stderr:
                line_str = LogLine(line.decode("utf-8"))
                record = LogRecord(
                    type=RecordType.stderr,
                    task_id=self._task_id,
                    task_name=self._task_name,
                    line=line_str,
                )
                self._log_records.append(record)
                self._notify_observers()
