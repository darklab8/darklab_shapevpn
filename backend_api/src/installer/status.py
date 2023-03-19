# write keeping status in Redis
from enum import Enum

from pydantic import BaseModel
from typing_extensions import Self

from backend_api.src.core import settings as conf
from backend_api.src.types import TaskID
from server_installer.src.storage.redis import RedisBase, SuffixType


class StatusState(str, Enum):
    PENDING = "PENDING"
    PROGRESS = "PROGRESS"
    SUCCESS = "SUCCESS"


class StatusData(BaseModel):
    state: StatusState = StatusState.PENDING
    total: int = conf.INSTALLER_MAX_TASKS
    current_number: int = 0
    current_name: str = ""


class RedisBackend(RedisBase):
    suffix_status: SuffixType = SuffixType("status")

    def set_status(self, status: StatusData) -> None:
        self._set(status.json(), self.suffix_status)

    def get_status(self) -> StatusData:
        data = self._get(self.suffix_status)

        if data is None:
            return StatusData()

        return StatusData.parse_raw(data)

    @classmethod
    def create(cls, task_id: TaskID) -> Self:
        return cls(
            redis_host=conf.REDIS_RESULT_HOST,
            redis_port=conf.REDIS_RESULT_PORT,
            redis_pass=conf.REDIS_RESULT_PASSWORD,
            task_id=task_id,
        )
