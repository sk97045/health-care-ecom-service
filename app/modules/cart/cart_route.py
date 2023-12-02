from fastapi import APIRouter
from bson import ObjectId
from app.modules.cart.cart_model import cartModel, CartSchema
router = APIRouter()

@router.post("/create")
async def create_cart(body:CartSchema):
    document = body.dict()
    cart_id = str(ObjectId())
    document["cart_id"] = cart_id
    await cartModel.createDocument(document)
    result = await cartModel.readDocument({"cart_id":cart_id})
    return {"success":True,"message":"Cart Created Successfully", "data": result}