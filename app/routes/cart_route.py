from bson import ObjectId
from fastapi import APIRouter

from app.models.cart_model import cart_model, CartSchema

router = APIRouter()

@router.post("/create")
async def create_cart(body:CartSchema):
    document = body.dict()
    cart_id = str(ObjectId())
    document["cart_id"] = cart_id
    await cart_model.createDocument(document)
    result = await cart_model.readDocument({"cart_id":cart_id})
    return {"success":True,"message":"Cart Created Successfully", "data": result}