from . import types as t
from .capturer import Capturer, Observer


class TestObserver:
    def notify(self, task_id: t.TaskID, log_record: t.LogRecord) -> None:
        self.remembered_record = log_record


def test_capturer() -> None:
    task_name = t.TaskName("abc")
    task_id = t.TaskID("123")

    capturer = Capturer(t.Command("echo 123\necho 456"), task_id, task_name)
    observer: Observer = TestObserver()
    capturer.register_observer(observer)
    capturer.run()

    assert observer.remembered_record == t.LogRecord( # type: ignore[attr-defined]
        type=t.RecordType.stdout,
        line=t.LogLine("456\n"),
        task_name=task_name,
        task_id=task_id,
    )
