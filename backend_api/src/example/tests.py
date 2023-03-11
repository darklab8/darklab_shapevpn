import pytest
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_ping_example(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "pong!"}
