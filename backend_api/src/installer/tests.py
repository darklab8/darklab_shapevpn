import pytest
from fastapi.testclient import TestClient
from backend_api.src.types import PingResponce


@pytest.mark.asyncio
async def test_ping_example(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == PingResponce.ping()
