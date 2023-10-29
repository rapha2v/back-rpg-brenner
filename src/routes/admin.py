from fastapi import APIRouter, Depends
from src.models import DefaultResponse

__all__ = ["Admin"]


Admin = APIRouter(
    prefix="/admin",
    tags=["Administracão"]
)


@Admin.get(
    path="/",
    response_model_exclude_unset=True,
    response_model=DefaultResponse
)
def rota_admin():
    return DefaultResponse(
        status=True,
        message="Tá funcionando"
    )
