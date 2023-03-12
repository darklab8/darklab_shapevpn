from pathlib import Path
from typing import AsyncGenerator

import docker  # type: ignore[import]
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from httpx import AsyncClient

from backend_api.src.core.main import app_factory


@pytest.fixture()
def app() -> FastAPI:
    app = app_factory()
    return app


@pytest.fixture()
def client(app: FastAPI) -> TestClient:
    client = TestClient(app)
    return client


@pytest.fixture()
async def async_client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client


@pytest.fixture()
def installer_image() -> str:
    client = docker.from_env()

    image_name = "server_installer_autouse"
    client.images.build(
        path=str(Path(__file__).parent.parent.parent / "server_installer"),
        tag=image_name,
    )
    return image_name
