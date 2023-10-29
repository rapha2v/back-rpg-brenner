from bson.objectid import ObjectId

__all__ = ["ObjectIdField"]


class ObjectIdField(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            type="string",
            example="6388a3af06778bbf4608e787"
        )

    @classmethod
    def validate(cls, v: ObjectId) -> ObjectId:
        if not ObjectId.is_valid(v):
            raise ValueError(f"{v} não é um ObjectId válido")
        return ObjectId(v)
