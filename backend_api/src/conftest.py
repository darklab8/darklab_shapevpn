from typing import AsyncGenerator

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
