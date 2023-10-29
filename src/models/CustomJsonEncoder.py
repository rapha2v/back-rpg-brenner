import json
from bson import ObjectId

__all__ = ["CustomJsonEncoder"]


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
