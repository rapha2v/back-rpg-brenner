from fastapi import APIRouter, Depends
from src.models import DefaultResponse
from .models.PersonagemRouter import ParamPersonagem

__all__ = ["Personagem"]


Personagem = APIRouter(
    prefix="/personagem",
    tags=["Personagem"]
)


@Personagem.get(
    path="/",
    response_model_exclude_unset=True,
    response_model=DefaultResponse
)
def rota_personagem(params: ParamPersonagem = Depends()):
    return DefaultResponse(
        status=True,
        message="Tá funcionando"
    )
