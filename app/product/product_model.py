from pydantic import BaseModel, Field, BeforeValidator
from app.config.mongo_config import vikingsHealthCareDatabase
from app.utils.mongo_util import MongoDbUtil
from typing_extensions import Annotated
from datetime import datetime

def check_price(price : float):
    assert price > 0, f'price {price} should be greater than 0.'
    return price

def check_units(unit_count : int):
    assert unit_count % 1 == 0, f'unit_count {unit_count} should be greater than equal to 0 and whole number.'
    return unit_count

ValidPrice = Annotated[float, BeforeValidator(check_price)]
ValidUnits = Annotated[int, BeforeValidator(check_units)]

"""
Container for a creating a single product record.
"""
class CreateProductRequest(BaseModel):
    name: str = Field(..., description="Name of the product")
    category: str = Field(..., description="Category of the product")
    price: ValidPrice = Field(..., description="Price of the product")
    units_available: ValidUnits = Field(..., description="Units available of the product")
    created_at: datetime = datetime.today()

"""
Container for a response from create product.
"""
class CreateProductResponse(BaseModel):
    product_id: str = Field(..., description="Id of the created product")
    message: str = Field(..., description="message")

"""
Container for a updating a single product record.
"""
class UpdateProductRequest(BaseModel):
    name: str | None = Field(description="Updated name")
    category: str | None = Field(description="Updated category")
    price: ValidPrice | None = Field(description="Updated price", ge=0)
    units_available: ValidUnits | None = Field(description="Updated unit count", ge=0)
    updated_at: datetime = datetime.today()

"""
Container for a response from create product.
"""
class UpdateProductResponse(BaseModel):
    product_id: str = Field(..., description="Id of the created product")
    message: str = Field(..., description="message")

product_model = MongoDbUtil(vikingsHealthCareDatabase["product"])