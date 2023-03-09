import os
import base64
import json
from zipfile import ZipFile
from os.path import basename
from pathlib import Path
from typing import Generator, Tuple


def decoder(data: str) -> bytes:
    return base64.b64decode(data.encode("utf-8"))


def encoder(data: bytes) -> str:
    encoded = base64.b64encode(data)
    return encoded.decode("utf-8")


def get_encoded_from_file(path: Path) -> str:
    with open(str(path), "rb") as file_:
        encoded = encoder(file_.read())
    return encoded


def file_paths(folder_path: Path) -> Generator[Tuple[str, Path], None, None]:
    for root, subdirs, files in os.walk(str(folder_path)):
        for file in files:
            yield file, Path(root) / file


def zip_files(folder_path: Path) -> str:
    filename = "sampleDir.zip"
    with ZipFile(filename, "w") as zipObj:
        for file, path in file_paths(folder_path):
            zipObj.write(path, basename(path))

    with open(filename, "rb") as file_:
        data = file_.read()

    os.remove(filename)

    return encoder(data)


def get_json_of_configs(folder_path: Path) -> str:
    result = {}

    for file, path in file_paths(folder_path):
        result[file] = get_encoded_from_file(path)

    result["zip"] = zip_files(folder_path)

    return json.dumps(result)
