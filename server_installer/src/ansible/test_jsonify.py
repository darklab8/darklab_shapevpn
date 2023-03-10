import json
import os
from pathlib import Path
from typing import Any, Dict

import pytest

from .. import exceptions
from . import configs, jsonify
from .configs import verify_configs_existence


@pytest.fixture
def config_path() -> Path:
    return Path(__file__).parent / "testdata" / "configs"


def test_verificator(config_path: Path) -> None:
    assert configs.verify_configs_existence(config_path)


def test_jsonify_configs(config_path: Path) -> None:
    result = jsonify.get_json_of_configs(config_path)
    dictionary_: Dict[str, Any] = json.loads(result)

    assert "1.conf" in dictionary_.keys()


def test_find_configs(config_path: Path) -> None:
    if not verify_configs_existence(config_path):
        raise exceptions.NotFound()


@pytest.mark.skip("too long test")
def test_everything() -> None:
    os.system("make build")
    os.system("make acceptance")


def test_jsonify_configs2(config_path: Path) -> None:
    jsonified = jsonify.get_json_of_configs(config_path)

    data = json.loads(jsonified)

    assert "zip" in data
    assert "1.conf" in data
    assert "1.png" in data

    print(data)
