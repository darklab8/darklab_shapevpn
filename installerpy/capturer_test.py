from . import types
from .capturer import Capturer, Observer


class StdoutObserver:
    def notify(self, task_id: types.TaskID, log_records: list[types.LogRecord]) -> None:
        print(log_records[-1].model_dump())


def test_capturer() -> None:
    task_name = types.TaskName("abc")
    task_id = types.TaskID("123")

    capturer = Capturer(types.Command("echo 123\necho 456"), task_id, task_name)
    observer: Observer = StdoutObserver()
    capturer.register_observer(observer)
    capturer.run()

    assert capturer._log_records[-1] == types.LogRecord(
        type=types.RecordType.stdout,
        line=types.LogLine("456\n"),
        task_name=task_name,
        task_id=task_id,
    )
