import logging
import os
from pathlib import Path
import json
from typing import Any

project_path = Path(__file__).parent.parent

log_levels: dict = {"": logging.WARN}
log_levels.update(logging._nameToLevel)

log_level = log_levels[os.environ.get("SHAPEVPN_LOG_LEVEL","")]
is_json_logged = os.environ.get("SHAPEVPN_LOG_JSON","false").lower() == "true"

logger_root = logging.getLogger("").getChild("")

def get_logger(file: str) -> logging.Logger:
    name = Path(file).relative_to(project_path)
    return logger_root.getChild(str(name))

def configure_logger(logger: logging.Logger) -> None:
    logger.setLevel(log_level)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    if is_json_logged:
        formatter = logging.Formatter('{"time":"%(asctime)s","filepath":"%(name)s","level":"%(levelname)s","content":%(message)s}')
    else:
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class StructuredMessage:
    def __init__(self, message: str, /, **kwargs: str | dict) -> None:
        self.message = message
        self.kwargs = kwargs

    def __str__(self) -> str:
        if is_json_logged:
            return json.dumps({"message":self.message,**self.kwargs})
        
        if len(self.kwargs.keys()) == 0:
            return self.message

        return '%s >>> %s' % (self.message, json.dumps(self.kwargs))

s = StructuredMessage

logger_root.setLevel(log_level)
