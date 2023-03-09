import pytest
from .storage import redis
from .interface import ui
from .storage.encryptor import SymmetricEncryptor


@pytest.fixture
def redis_conn() -> redis.Redis:
    return redis.Redis(
        input=ui.RedisInput(
            redis_host="localhost",
            redis_pass="",
            redis_port=6379,
            encryption_key=SymmetricEncryptor.generate_key().decode("utf-8"),
            task_id="456",
        )
    )
