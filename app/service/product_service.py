from fastapi import HTTPException, status
from app.config.mongo_config import vikings_health_care_database
from app.utils.mongo_util import MongoDbUtil
from app.request_models.product_model import *
from app.schema_types.product import *

product_collection = MongoDbUtil(vikings_health_care_database["product"])

class ProductService:
    async def create_product(product: CreateProductRequest):
        document = Product(**product.model_dump(by_alias=True))
        created_product =  await product_collection.createDocument(document)
        return created_product
       
    async def get_product(product_id: str):
        document = {"_id":product_id}
        product = await product_collection.readDocument(document)
        if product is not None:
            return product
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"No product found for product_id {product_id}")

    async def get_all_products(page_size: int):
        products = await product_collection.getDocuments({}, pageSize=page_size)
        return products

    async def update_product(product_id: str, product: UpdateProductRequest):
        document = product.model_dump(by_alias=True)
        fields_to_update = {
            k: v for k, v in document.items() if v is not None
        }

        if len(fields_to_update) >= 1:
            update_result = await product_collection.updateDocument(
                {"_id": product_id}, {"$set": fields_to_update})
            if update_result is not None:
                return update_result
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"No product found for product_id {product_id}")
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Nothing to update for the product_id {product_id}")
    
    async def delete_product(product_id: str, product: UpdateProductRequest):
        document = product.model_dump(by_alias=True)
        fields_to_update = {
            k: v for k, v in document.items() if v is not None
        }

        if len(fields_to_update) >= 1:
            update_result = await product_collection.updateDocument(
                {"_id": product_id}, {"$set": fields_to_update})
            
            return update_result
            
        # The update is empty, but we should still return the matching document:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"Nothing to update for the product with id {product_id}")