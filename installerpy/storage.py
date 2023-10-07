import redis

from . import types as t
from .settings import settings
from . import log as l

logger = l.get_logger(__file__)

class Redis:
    def __init__(self) -> None:
        self._client = redis.Redis(
            host=settings.redis_host, port=settings.redis_port, db=0
        )

    def notify(self, task_id: t.TaskID, log_record: t.LogRecord) -> None:
        logger.debug(l.s("yielding record to redis",log_record=log_record.model_dump()))
        self._client

