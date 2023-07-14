import pytest

from server_installer.src.conftest import RedisConnData, redis_conn_data

from .src.installer.status import RedisBackend

_ = redis_conn_data


@pytest.fixture
def redis_backend(redis_conn_data: RedisConnData) -> RedisBackend:
    return RedisBackend(**redis_conn_data)
