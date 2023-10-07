from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

from . import types as t

project_path = Path(__file__).parent.parent

class Settings(BaseSettings):
    redis_host: t.RedisHost = t.RedisHost("localhost")
    redis_port: t.RedisPort = t.RedisPort(6379)

    model_config = SettingsConfigDict(env_prefix="shapevpn_")

settings = Settings()
