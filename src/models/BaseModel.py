import json

from pydantic import BaseModel as PydanticBaseModel, Extra

from bson.objectid import ObjectId
from pymongo.cursor import Cursor

from src.models.CustomJsonEncoder import CustomJsonEncoder

__all__ = ['BaseModel']


class BaseModel(PydanticBaseModel):
    """
    Classe usada de base para a criação dos schemas pydantic.

    - É uma versão extendida de `pydantic.BaseModel`, contendo algumas
      configurações padronizadas para o projeto.
    """
    class Config:
        extra = Extra.forbid
        json_encoders = {
            ObjectId: lambda x: str(x),
            Cursor: lambda x: [json.loads(CustomJsonEncoder().encode(y)) for y in x]
        }
        smart_union = True
