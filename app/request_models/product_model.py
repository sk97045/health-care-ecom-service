from datetime import datetime
from pydantic import BaseModel, Field, BeforeValidator
from typing import List
from typing_extensions import Annotated
from app.utils.product_type_validators import ProductTypesCustomValidtors


valid_price = Annotated[float, BeforeValidator(ProductTypesCustomValidtors.check_price)]
valid_units = Annotated[int, BeforeValidator(ProductTypesCustomValidtors.check_units)]

"""
Container for a creating a single product record.
"""
class CreateProductRequest(BaseModel):
    name: str = Field(..., description="Name of the product")
    category: str = Field(..., description="Category of the product")
    price: valid_price = Field(..., description="Price of the product")
    units_available: valid_units = Field(..., description="Units available of the product")

"""
Container for a updating a single product record.
"""
class UpdateProductRequest(BaseModel):
    name: str | None = Field(description="Updated name")
    category: str | None = Field(description="Updated category")
    price: valid_price | None = Field(description="Updated price")
    units_available: valid_units | None = Field(description="Updated unit count")

"""
Container for a response from create product. 
"""
class ProductDetails(BaseModel):
    product_id: str = Field(..., description="Id of the created product")
    name: str = Field(..., description="Name of the product")
    category: str = Field(..., description="Category of the product")
    price: valid_price = Field(..., description="Price of the product")
    units_available: valid_units = Field(..., description="Units available of the product")
    created_at: datetime = Field(..., description="Time when product details were first created")
    updated_at: datetime | None = Field(description="Time when product was last updated")

"""
Container for a multiple product details.
"""
class ListofProductDetails(BaseModel):
    products: List[ProductDetails] = Field(..., description="First N products details")
