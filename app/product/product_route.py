from fastapi import APIRouter, Body, HTTPException, status, Response
from bson import ObjectId
from pymongo import ReturnDocument
from app.utils.response_handler import OK
from app.product.product_model import product_model, CreateProductRequest, CreateProductResponse, UpdateProductRequest, UpdateProductResponse


router = APIRouter()

@router.post("/product", 
             response_description="Add new product to health database",
             response_model=CreateProductResponse,
             status_code=status.HTTP_201_CREATED,
             response_model_by_alias=False,)
async def create_product(product: CreateProductRequest):
    create_product =  await product_model.createDocument(product.model_dump(by_alias=True))
    if create_product.acknowledged and OK(create_product.insertedId):
        createProductResponse = CreateProductResponse(id= str(create_product.insertedId), message="Product Created Successfully")
        return createProductResponse
    else:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=create_product) 


@router.post("/product/{productid}", 
             response_description="Add new product to health database",
             response_model=UpdateProductResponse,
             response_model_by_alias=True,)
async def update_product(productid: str, product: UpdateProductRequest = Body(...)):
    product = {
        k: v for k, v in product.model_dump(by_alias=True).items() if v is not None
    }

    if len(product) >= 1:
        update_result = await product_model.updateDocument(
            {"_id": productid}, {"$set": product}, return_document=ReturnDocument.AFTER)
        
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Product with id {productid} not found")

    # The update is empty, but we should still return the matching document:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Nothing to update for the product with id {productid}")

