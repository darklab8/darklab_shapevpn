from pydantic_settings import BaseSettings, SettingsConfigDict

from . import types


class Settings(BaseSettings):
    redis_host: types.RedisHost = types.RedisHost("localhost")
    redis_port: types.RedisPort = types.RedisPort(6379)

    model_config = SettingsConfigDict(env_prefix="shapevpn_")


settings = Settings()
