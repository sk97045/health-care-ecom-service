from typing import Annotated, Any

from bson import ObjectId
from pydantic import BaseModel, ConfigDict, AfterValidator, GetPydanticSchema, PlainSerializer, WithJsonSchema


class MongoDBObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid MongoDB ObjectId')
        return str(v)


class PydanticModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
