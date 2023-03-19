import logging
from typing import Any, Dict

from celery.app.task import Task

from backend_api.src.installer import measurer
from backend_api.src.installer.tasks import InstallServerTask, ProtectedSerializer
from backend_api.src.types import TaskID
from server_installer.src.utils import logger

Task.__class_getitem__ = classmethod(  # type: ignore[attr-defined]
    lambda cls, *args, **kwargs: cls
)

from celery import Celery

from ..installer.tasks import debug_my_task

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


@app.task(bind=True)
def task_vpn_install(
    self: Task, user_input: Dict[str, Any], unique_id: str = "undefined"
) -> str:
    print(123)
    logging.info(f"unique_id={unique_id}, task_vpn_install begins")
    start_time = measurer.start_time_measuring()
    task_id = self.request.id

    InstallServerTask(
        task=self,
        start_time=start_time,
        unique_id=unique_id,
        task_id=TaskID(task_id),
        user_input=ProtectedSerializer.deserialize(**user_input),
    ).run()
    return f"succesful_installation_{unique_id}"


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs: dict[str, str]) -> None:
    sender.add_periodic_task(seconds_repeat, loop_task.s(), expires=10)
