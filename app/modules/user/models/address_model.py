from typing import Optional, List

from pydantic import Field

from app.utils.pydantic_model import PydanticModel, MongoDBObjectId


class AddressModel(PydanticModel):
    id: MongoDBObjectId = Field()
    address_line_1: str = Field()
    address_line_2: Optional[str] = Field(default=None)
    city: str = Field()
    district: str = Field()
    state: str = Field()
    country: str = Field()
    postal_code: str = Field()
    is_primary: Optional[bool] = Field(default=False)


class CreateAddressModel(PydanticModel):
    address_line_1: str = Field()
    address_line_2: Optional[str] = Field(default=None)
    city: str = Field()
    district: str = Field()
    state: str = Field()
    country: str = Field()
    postal_code: str = Field()
    is_primary: Optional[bool] = Field(default=False)


class UpdateAddressModel(PydanticModel):
    address_line_1: Optional[str] = Field()
    address_line_2: Optional[str] = Field()
    city: Optional[str] = Field()
    district: Optional[str] = Field()
    state: Optional[str] = Field()
    country: Optional[str] = Field()
    postal_code: Optional[str] = Field()
    is_primary: Optional[bool] = Field()


class AddressCollection(PydanticModel):
    addresses: List[AddressModel]
