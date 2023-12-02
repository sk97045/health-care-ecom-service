from typing import Optional, List

from pydantic import Field, EmailStr, conlist

from app.modules.user.types.user_type import UserType
from app.modules.user.models.address_model import AddressModel
from app.utils.pydantic_model import PydanticModel, MongoDBObjectId


class UserModel(PydanticModel):
    id: MongoDBObjectId = Field()
    first_name: str = Field()
    last_name: Optional[str] = Field(default=None)
    primary_email: EmailStr = Field()
    secondary_email: Optional[EmailStr] = Field(default=None)
    primary_phone_number: str = Field()
    secondary_phone_number: Optional[str] = Field(default=None)
    user_type: Optional[UserType] = Field(default=UserType.CUSTOMER)
    addresses: conlist(item_type=Optional[AddressModel], min_length=0) = Field(default=[])


class CreateUserModel(PydanticModel):
    first_name: str = Field()
    last_name: Optional[str] = Field(default=None)
    primary_email: EmailStr = Field()
    secondary_email: Optional[EmailStr] = Field(default=None)
    primary_phone_number: str = Field()
    secondary_phone_number: Optional[str] = Field(default=None)
    user_type: Optional[UserType] = Field(default=UserType.CUSTOMER)


class UpdateUserModel(PydanticModel):
    first_name: Optional[str] = Field()
    last_name: Optional[str] = Field()
    primary_email: Optional[EmailStr] = Field()
    secondary_email: Optional[EmailStr] = Field()
    primary_phone_number: Optional[str] = Field()
    secondary_phone_number: Optional[str] = Field()


class UserCollection(PydanticModel):
    users: List[UserModel]
