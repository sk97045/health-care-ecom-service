from typing import Optional, List

from pydantic import BaseModel, Field, EmailStr, conlist

from app.modules.user.types.user_type import UserType
from app.modules.user.models.address_model import AddressModel
from app.utils.pydantic_model import PydanticModel, MongoDBObjectId


class UserModel(PydanticModel):
    id: MongoDBObjectId = Field()
    firstName: str = Field()
    lastName: Optional[str] = Field(default=None)
    primaryEmail: EmailStr = Field()
    secondaryEmail: Optional[EmailStr] = Field(default=None)
    primaryPhoneNumber: str = Field()
    secondaryPhoneNumber: Optional[str] = Field(default=None)
    userType: Optional[UserType] = Field(default=UserType.CUSTOMER)
    addresses: conlist(item_type=Optional[AddressModel], min_length=0) = Field(default=[])


class CreateUserModel(PydanticModel):
    firstName: str = Field()
    lastName: Optional[str] = Field(default=None)
    primaryEmail: EmailStr = Field()
    secondaryEmail: Optional[EmailStr] = Field(default=None)
    primaryPhoneNumber: str = Field()
    secondaryPhoneNumber: Optional[str] = Field(default=None)
    userType: Optional[UserType] = Field(default=UserType.CUSTOMER)


class UpdateUserModel(PydanticModel):
    firstName: Optional[str] = Field()
    lastName: Optional[str] = Field()
    primaryEmail: Optional[EmailStr] = Field()
    secondaryEmail: Optional[EmailStr] = Field()
    primaryPhoneNumber: Optional[str] = Field()
    secondaryPhoneNumber: Optional[str] = Field()


class UserCollection(PydanticModel):
    users: List[UserModel]
