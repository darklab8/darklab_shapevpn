from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import backend_api.src.installer.views as example_views
from server_installer.src.utils import logger

from ..types import PingResponce


def app_factory() -> FastAPI:
    logger.configure()
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(example_views.router_example)
    app.include_router(example_views.router_install)

    @app.get("/")
    def get_ping() -> PingResponce:
        return PingResponce.ping()

    return app


if "main" in __name__:
    app = app_factory()
