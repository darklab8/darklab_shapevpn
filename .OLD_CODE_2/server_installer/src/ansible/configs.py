import os
from pathlib import Path


def verify_configs_existence(folder_path: Path) -> bool:
    for root, subdirs, files in os.walk(folder_path):
        if len(files) > 0:
            return True
    else:
        raise FileNotFoundError("configs were not found")
