from celery.app.task import Task

from server_installer.src.utils import logger

Task.__class_getitem__ = classmethod(  # type: ignore[attr-defined]
    lambda cls, *args, **kwargs: cls
)

from celery import Celery

from ..installer.tasks import task_vpn_install

logger.configure()
from . import settings as conf

app = Celery(
    "core",
    broker=conf.REDIS_QUEUE,
    backend=conf.REDIS_RESULT,
)

app.conf.broker_url = conf.REDIS_QUEUE
app.conf.result_backend = conf.REDIS_RESULT

from .tasks import loop_task

seconds_repeat = 30.0


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs: dict[str, str]) -> None:
    sender.add_periodic_task(seconds_repeat, loop_task.s(), expires=10)
