from . import redis
from .config_encryptor import ConfigEncryptor


def test_encryptor(redis_conn: redis.Redis) -> None:
    data = "abc"
    secret_key = ConfigEncryptor.generate_key().decode("utf-8")
    redis_conn.set_config(data, secret_key)
    assert redis_conn.get_config(secret_key) == data
    assert redis_conn._redis.get(f"456_{redis.Redis.config_suffix}") != data
