from typing import Optional, Any
from pydantic import root_validator
from src.models.BaseModel import BaseModel


class DefaultResponse(BaseModel):
    status: bool
    data: Optional[dict] = None
    message: Optional[str] = None

    @root_validator(pre=True)
    def validate_params(cls, values: dict):  # noqa
        if not values.get("data") and not values.get("message"):
            raise AttributeError("Não possui o atributo 'data' ou 'message'")
        return values
