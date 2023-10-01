import redis

from . import types
from .settings import settings


class Redis:
    def __init__(self) -> None:
        self._client = redis.Redis(
            host=settings.redis_host, port=settings.redis_port, db=0
        )

    def notify(self, task_id: types.TaskID, log_records: list[types.LogRecord]) -> None:
        pass
