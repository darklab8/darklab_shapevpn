from fastapi.testclient import TestClient

from backend_api.src.types import PingResponce


def test_read_main(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == PingResponce.ping()
