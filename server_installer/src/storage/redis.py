from typing import Any, NewType, Union

import redis

from .. import exceptions
from ..interface import ui
from .config_encryptor import ConfigEncryptor

SuffixType = NewType("SuffixType", str)


class RedisBase:
    _redis: redis.Redis
    _active: bool

    def __init__(
        self, redis_host: str, redis_port: int, redis_pass: str, task_id: str
    ) -> None:
        self._redis_host = redis_host

        self._task_id = task_id
        self._redis = redis.Redis(
            host=redis_host,
            password=redis_pass,
            port=redis_port,
            db=0,
        )
        self._active = True

    @property
    def active(self) -> bool:
        return self._redis_host != "" and self._task_id != ""

    def _set(self, data: str, suffix_key: SuffixType) -> None:
        if not self._active:
            raise exceptions.RedisConnectionFaliure("redis connection is not active")

        if not self._task_id:
            raise exceptions.RedisConnectionFaliure("task_id is not defined")

        self._redis.set(f"{self._task_id}_{suffix_key}", data)
        print(
            f"task_id={self._task_id}, object={suffix_key} was sent to nosql database"
        )

    def _get(self, suffix_key: SuffixType) -> Union[Any, None]:
        return self._redis.get(f"{self._task_id}_{suffix_key}")


class RedisInstaller(RedisBase):
    stdout_suffix: SuffixType = SuffixType("stdout")
    config_suffix: SuffixType = SuffixType("config")

    def set_stdout(self, data: str) -> None:
        self._set(data, self.stdout_suffix)

    def get_stdout(self) -> Union[str, None]:
        return self._get(self.stdout_suffix)

    def set_config(self, data: str, configs_encryption_key: str) -> None:
        encryptor = ConfigEncryptor(configs_encryption_key)
        encrypted_data = encryptor.encrypt_str(data)
        self._set(encrypted_data, self.config_suffix)

    def get_config(self, configs_encryption_key: str) -> Union[str, None]:
        data = self._get(self.config_suffix)
        if data is None:
            return None

        encryptor = ConfigEncryptor(configs_encryption_key)
        decrypted = encryptor.decrypt_bytes(data).decode("utf-8")
        return decrypted
