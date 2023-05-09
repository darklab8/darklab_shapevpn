from celery.app.task import Task

Task.__class_getitem__ = classmethod(  # type: ignore[attr-defined]
    lambda cls, *args, **kwargs: cls
)

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.core.settings")

app = Celery(
    "core",
    broker=settings.REDIS_QUEUE,
    backend=settings.REDIS_RESULT,
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.broker_url = settings.REDIS_QUEUE
app.conf.result_backend = settings.REDIS_RESULT

from ..installer.tasks import loop_task


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs: dict[str, str]) -> None:
    sender.add_periodic_task(seconds_repeat := 30, loop_task.s(), expires=10)
