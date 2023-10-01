"""
Captures shell output and puts to somewhere
"""
import subprocess
from typing import Protocol

from typing_extensions import Self

from . import types


class Observer(Protocol):
    def notify(self, task_id: types.TaskID, log_records: list[types.LogRecord]) -> None:
        ...


class Capturer:
    def __init__(
        self,
        cmd: types.Command,
        task_id: types.TaskID,
        task_name: types.TaskName,
    ):
        self._cmd = cmd
        self._task_id = task_id
        self._task_name = task_name
        self._observers: list[Observer] = []
        self._log_records: list[types.LogRecord] = []

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
            line_str = types.LogLine(line.decode("utf-8"))
            record = types.LogRecord(
                type=types.RecordType.stdout,
                task_id=self._task_id,
                task_name=self._task_name,
                line=line_str,
            )
            self._log_records.append(record)
            self._notify_observers()

        proc.wait()

        if proc.stderr is not None:
            for line in proc.stderr:
                line_str = types.LogLine(line.decode("utf-8"))
                record = types.LogRecord(
                    type=types.RecordType.stderr,
                    task_id=self._task_id,
                    task_name=self._task_name,
                    line=line_str,
                )
                self._log_records.append(record)
                self._notify_observers()
