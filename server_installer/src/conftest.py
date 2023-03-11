import os

import pytest

from .interface import ui
from .storage import redis
from .storage.config_encryptor import ConfigEncryptor

test_redis_host = os.environ.get("test_redis_host", "localhost")


@pytest.fixture
def redis_conn() -> redis.Redis:
    return redis.Redis(
        input=ui.RedisInput(
            redis_host=test_redis_host,
            redis_pass="",
            redis_port=6379,
            configs_encryption_key=ConfigEncryptor.generate_key().decode("utf-8"),
            task_id="456",
        )
    )
