import logging

from celery import Celery, shared_task

logger = logging.getLogger(__name__)


@shared_task
def loop_task() -> bool:
    logger.info(f"ping is done")
    return True
