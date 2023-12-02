from typing import Optional, List

from pydantic import Field

from app.utils.pydantic_model import PydanticModel, MongoDBObjectId


class AddressModel(PydanticModel):
    id: MongoDBObjectId = Field()
    addressLine1: str = Field()
    addressLine2: Optional[str] = Field(default=None)
    city: str = Field()
    district: str = Field()
    state: str = Field()
    country: str = Field()
    postalCode: str = Field()
    isPrimary: Optional[bool] = Field(default=False)


class CreateAddressModel(PydanticModel):
    addressLine1: str = Field()
    addressLine2: Optional[str] = Field(default=None)
    city: str = Field()
    district: str = Field()
    state: str = Field()
    country: str = Field()
    postalCode: str = Field()
    isPrimary: Optional[bool] = Field(default=False)


class UpdateAddressModel(PydanticModel):
    addressLine1: Optional[str] = Field()
    addressLine2: Optional[str] = Field()
    city: Optional[str] = Field()
    district: Optional[str] = Field()
    state: Optional[str] = Field()
    country: Optional[str] = Field()
    postalCode: Optional[str] = Field()
    isPrimary: Optional[bool] = Field()


class AddressCollection(PydanticModel):
    addresses: List[AddressModel]
