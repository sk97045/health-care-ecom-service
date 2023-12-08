from datetime import datetime
from pydantic import BaseModel, Field, BeforeValidator
from typing import List, Optional
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
    description: str = Field(..., description="Description of the product")
    price: valid_price = Field(..., description="Price of the product")
    units_available: valid_units = Field(..., description="Units available of the product")

"""
Container for a updating a single product record.
"""
class UpdateProductRequest(BaseModel):
    name: str | None = Field(description="Updated name", default=None)
    category: str | None = Field(description="Updated category", default=None)
    description: str | None = Field(description="Description of the product", default=None)
    price: valid_price | None = Field(description="Updated price", default=None)
    units_available: valid_units | None = Field(description="Updated unit count", default=None)

"""
Container for a response from create product. 
"""
class ProductDetails(BaseModel):
    id: Optional[str] = Field(description="Id of the product", default=None)
    name: Optional[str] = Field(description="Name of the product", default=None)
    category: Optional[str] = Field(description="Category of the product", default=None)
    description: Optional[str] = Field(description="Description of the product", default=None)
    price: valid_price = Field(description="Price of the product", default=None)
    units_available: valid_units = Field(description="Units available of the product", default=None)
    created_at: Optional[datetime] = Field(description="Time when product was first created", default=None)
    updated_at: Optional[datetime] = Field(description="Time when product was last updated", default=None)

"""
Container for a multiple product details.
"""
class ListofProductDetails(BaseModel):
    products: List[ProductDetails] | None = Field(description="First N products details")
