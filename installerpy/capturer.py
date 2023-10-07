"""
Captures shell output and puts to somewhere
"""
import subprocess
from typing import Protocol

from typing_extensions import Self

from . import types as t
from . import log as l

logger = l.get_logger(__file__)

class Observer(Protocol):
    def notify(self, task_id: t.TaskID, log_records: t.LogRecord) -> None:
        ...


class Capturer:
    def __init__(
        self,
        cmd: t.Command,
        task_id: t.TaskID,
        task_name: t.TaskName,
    ):
        self._cmd = cmd
        self._task_id = task_id
        self._task_name = task_name
        self._observers: list[Observer] = []

    def register_observer(self, observer: Observer) -> Self:
        self._observers.append(observer)
        return self

    def _notify_observers(self, record: t.LogRecord) -> None:
        for observer in self._observers:
            observer.notify(self._task_id, record)

    def run(self) -> None:
        logger.debug(l.s(f"opening Popen", cmd=self._cmd))
        proc = subprocess.Popen(
            self._cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
        )

        assert proc.stdout is not None

        for line in proc.stdout:
            line_str = t.LogLine(line.decode("utf-8"))
            record = t.LogRecord(
                type=t.RecordType.stdout,
                task_id=self._task_id,
                task_name=self._task_name,
                line=line_str,
            )
            self._notify_observers(record)

        logger.debug("awaiting to finish proc")
        proc.wait()

        if proc.stderr is not None:
            for line in proc.stderr:
                line_str = t.LogLine(line.decode("utf-8"))
                record = t.LogRecord(
                    type=t.RecordType.stderr,
                    task_id=self._task_id,
                    task_name=self._task_name,
                    line=line_str,
                )
                self._notify_observers(record)

