from django.http import HttpRequest
from ninja import NinjaAPI

from backend.backend_types import PingResponce

api = NinjaAPI()


@api.get("/ping")
def ping(request: HttpRequest) -> PingResponce:
    return PingResponce.ping()
