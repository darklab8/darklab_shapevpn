import logging
import os
from enum import Enum


class LoggerLevels(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO


def configure() -> None:
    level = LoggerLevels[os.environ.get("LOGGING_LEVEL", "DEBUG")]

    logging.basicConfig(
        format="%(levelname)s: %(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        level=level.value,
    )
