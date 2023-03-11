from fastapi import APIRouter
from typing import Dict

router = APIRouter(
    prefix="/example",
    tags=["items"],
)


@router.get(path="/")
async def ping() -> Dict[str, str]:
    return {"message": "pong"}
