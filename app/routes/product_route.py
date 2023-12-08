from fastapi import APIRouter, Body, HTTPException, status, Response
from app.service.product_service import ProductService
from app.models.product_model import *

router = APIRouter()
service = ProductService()

@router.post("/", 
             response_description="Added new product to health database",
             response_model=ProductDetails,
             status_code=status.HTTP_201_CREATED,
             response_model_by_alias=True,)
async def create_product(product: CreateProductRequest = Body(..., description="Product with relevant details")): 
    create_product = await service.create_product(product)
    return ProductDetails(**create_product) 


@router.get(
    "/{id}",
    response_description="Information for product with given product_id",
    response_model=ProductDetails,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
)
async def get_product(product_id: str):
    product = await service.get_product(product_id)
    return ProductDetails(**product)

@router.get(
    "/all/",
    response_description="Details for the requested products",
    response_model=ListofProductDetails,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=True,
)
async def get_all_products(pageSize: int | None = 0):
    print("pageSize is ", pageSize)
    products = await service.get_all_products(pageSize)
    if len(products) > 0:
        return ListofProductDetails(products=products)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/{productid}/", 
             response_description="Updated product to health database",
             response_model=ProductDetails,
             status_code=status.HTTP_200_OK,
             response_model_by_alias=True,)
async def update_product(
    productid: str, 
    updated_product_details: UpdateProductRequest = Body(..., description="Details to be updated in product")):
    update_result = await service.update_product(productid, updated_product_details)
    return ProductDetails(**update_result)
    

@router.delete("/{productid}", 
               response_description="Deleted a product with given product_id")
async def delete_product(product_id: str):
   return await service.delete_product(product_id)
    

