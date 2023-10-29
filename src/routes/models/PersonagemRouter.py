from src.models import BaseModel, ObjectIdField

__all__ = ["ParamPersonagem"]


class ParamPersonagem(BaseModel):
    oid: ObjectIdField

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True  # required for the _id
