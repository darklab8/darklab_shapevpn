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
