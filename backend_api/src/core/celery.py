import os

from celery.app.task import Task

Task.__class_getitem__ = classmethod(  # type: ignore[attr-defined]
    lambda cls, *args, **kwargs: cls
)

from celery import Celery

from ..installer.tasks import loop_task

config = os.environ

app = Celery(
    "core",
    broker=config.get("CACHE_BACKEND", "redis://redis:6379"),
    backend=config.get("CACHE_BACKEND", "redis://redis:6379"),
)

seconds_repeat = 30.0


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs: dict[str, str]) -> None:
    sender.add_periodic_task(seconds_repeat, loop_task.s(), expires=10)
