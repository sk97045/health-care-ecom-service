from pydantic import BaseModel
from app.config.mongo_config import database_client
from app.utils.mongo_util import MongoDbUtil

class CartItems(BaseModel):
    product_id: str
    title: str
    price: float
    
class CartSchema(BaseModel):
    user_id: str
    items: list[CartItems]
    
cart_model = MongoDbUtil(database_client["cart"])