from django.http import HttpRequest
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request: HttpRequest) -> str:
    return "Hello world"
