import pytest
from django.test import Client

from backend.backend_types import PingResponce


@pytest.fixture
def client() -> Client:
    return Client()


def test_read_main(client: Client) -> None:
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.json() == PingResponce.ping()
