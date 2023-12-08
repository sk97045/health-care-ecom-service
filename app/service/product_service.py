from bson import ObjectId, errors
from fastapi import status, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from app.config.mongo_config import database_client
from app.utils.mongo_util import MongoDbUtil
from app.models.product_model import *
from app.schema.product import *

product_collection = MongoDbUtil(database_client["product"])

class ProductService:
    @staticmethod
    async def create_product(product: CreateProductRequest):
        document = Product(**product.model_dump(by_alias=True))
        document.set_create_time(datetime.now())
        created_product =  await product_collection.create_document(jsonable_encoder(document))
        return created_product

    @staticmethod  
    async def get_product(product_id: str):
        document = {"_id":ObjectId(product_id)}
        product = await product_collection.read_document(document)
        if product is not None:
            return product
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"No product found for product_id {product_id}")
    
    @staticmethod
    async def get_all_products(page_size: int):
        products = await product_collection.fetch_documents(filter={}, pageSize=page_size)
        return products

    @staticmethod
    async def update_product(product_id: str, product: UpdateProductRequest):
        document = Product(**product.model_dump(by_alias=True))
        document.set_update_time(datetime.now())
        document = jsonable_encoder(document)

        fields_to_update = {
            k: v for k, v in document.items() if v is not None
        }

        if len(fields_to_update) >= 1:
            update_result = await product_collection.update_document(
                {"_id": ObjectId(product_id)}, {"$set": fields_to_update})
            if update_result is not None:
                return update_result
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"No product found for product_id {product_id}")
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Nothing to update for the product_id {product_id}")
    
    @staticmethod
    async def delete_product(product_id: str):
        try:
            product_id = ObjectId(product_id)
        except (errors.InvalidId, TypeError):
            raise ValueError(f"Invalid ObjectId: {id}")
        
        delete_result = await product_collection.delete_document({"_id": ObjectId(product_id)})

        if delete_result == 1:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Student {id} not found")