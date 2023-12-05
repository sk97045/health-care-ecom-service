from fastapi import APIRouter, Body, HTTPException, status, Response
from app.service.product_service import ProductService
from app.models.product_model import *

router = APIRouter()
service = ProductService()

@router.post("/product", 
             response_description="Add new product to health database",
             response_model=ProductDetails,
             status_code=status.HTTP_201_CREATED,
             response_model_by_alias=False,)
async def create_product(product: CreateProductRequest): 
    create_product = await service.create_product(product)
    return ProductDetails(**create_product.dict()) 


@router.get(
    "/product/{id}",
    response_description="Fetch information for product with given product_id",
    response_model=ProductDetails,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def get_product(product_id: str):
    product = await service.get_product(product_id)
    return ProductDetails(**product.dict())

@router.get(
    "/products}",
    response_description="List details about first N products",
    response_model=ListofProductDetails,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def get_all_products(pageSize: int | None = 0):
    products = await service.get_all_products()
    return ListofProductDetails(**products.dict())


@router.post("/product/{productid}", 
             response_description="Add new product to health database",
             response_model=ProductDetails,
             status_code=status.HTTP_200_OK,
             response_model_by_alias=True,)
async def update_product(
    productid: str, 
    updated_product_details: UpdateProductRequest = Body(..., description="Details to be updated in product")):
    update_result = await service.update_product(productid, updated_product_details)
    return ProductDetails(**update_result.dict())
    

@router.delete("/product/{productid}", 
               response_description="Delete a product with given product_id")
async def delete_product(product_id: int):
    delete_result = await service.delete_many({"productid": product_id})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Product {product_id} not found")

