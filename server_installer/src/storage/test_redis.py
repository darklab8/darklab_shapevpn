import secrets

from . import redis


def test_redis_works(redis_conn: redis.Redis) -> None:
    random_key = secrets.token_hex(16)

    redis_conn._redis.set(random_key, f"{random_key}123")

    data = redis_conn._redis.get(random_key)

    assert data is not None

    assert data.decode("utf-8") == f"{random_key}123"


def test_redis_works_with_bytes(redis_conn: redis.Redis) -> None:
    random_key = secrets.token_hex(16)

    input_data = b"my byte string"

    redis_conn._redis.set(random_key, input_data)

    extracted_data = redis_conn._redis.get(random_key)

    assert extracted_data == input_data
