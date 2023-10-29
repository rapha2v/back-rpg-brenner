from pydantic import Field
from typing import List
from bson import ObjectId
from src.models import ObjectIdField, BaseModel

__all__ = ["Multiplicadores", "HabilidadeAtiva", "HabilidadePassiva", "Habilidades", "Atributos"]


class Multiplicadores(BaseModel):
    atributo: str
    escala: int


class HabilidadeAtiva(BaseModel):
    nome: str
    descricao: str
    multiplicadores: List[Multiplicadores]


class HabilidadePassiva(BaseModel):
    nome: str
    descricao: str


class Habilidades(BaseModel):
    ativas: List[HabilidadeAtiva]
    passivas: List[HabilidadePassiva]


class Atributos(BaseModel):
    forca: int
    resistencia: int
    capacidade: int
    destreza: int
    inteligencia: int
    sabedoria: int
    sorte: int


class Parametros(BaseModel):
    hp: int
    mana: int


class PersonagemDB(BaseModel):
    _id: ObjectIdField = Field(alias="_id")
    nome: str
    level: int
    classe: str
    elemento: str
    atributos: Atributos
    itens: List[ObjectId]
    armas: List[ObjectId]
    habilidades: Habilidades

    class Config:
        arbitrary_types_allowed = True


class HabilidadeAtivaComDano(HabilidadeAtiva):
    dano: int


class HabilidadesComDano(Habilidades):
    ativas: List[HabilidadeAtivaComDano]


class PersonagemResponse(PersonagemDB):
    parametros: Parametros
    habilidades: HabilidadesComDano
