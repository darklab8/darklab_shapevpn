from . import redis


def test_encryptor(redis_conn: redis.Redis) -> None:
    data = "abc"
    redis_conn.set_config(data)
    assert redis_conn.get_config() == data
    assert redis_conn._redis.get(f"456_{redis.Redis.config_suffix}") != data
