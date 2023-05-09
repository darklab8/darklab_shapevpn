from typing import Type

from backend_api2.src.installer import status


def test_check_test(redis_backend: status.RedisBackend) -> None:
    stat = redis_backend.get_status()
    assert stat.state == status.StatusState.PENDING

    redis_backend.set_status(status.StatusData(state=status.StatusState.SUCCESS))
    stat = redis_backend.get_status()
    assert stat.state == status.StatusState.SUCCESS
