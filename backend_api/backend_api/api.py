from ninja import NinjaAPI
from django.http import HttpRequest

api = NinjaAPI()


@api.get("/hello")
def hello(request: HttpRequest) -> str:
    return "Hello world"
