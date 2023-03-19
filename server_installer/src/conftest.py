import os
import secrets
from typing import Any, Dict, TypedDict

import pytest

from .storage import redis

test_redis_host = os.environ.get("REDIS_RESULT_HOST", "localhost")


class RedisConnData(TypedDict):
    redis_host: str
    redis_pass: str
    redis_port: int
    task_id: str


@pytest.fixture
def redis_conn_data() -> RedisConnData:
    return dict(
        redis_host=test_redis_host,
        redis_pass="",
        redis_port=6379,
        task_id=secrets.token_hex(16),
    )


@pytest.fixture
def redis_conn(redis_conn_data: RedisConnData) -> redis.RedisInstaller:
    return redis.RedisInstaller(**redis_conn_data)
