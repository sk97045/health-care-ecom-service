from fastapi import APIRouter
from app.cart.cart_route import router as cart_router

router = APIRouter()

router.include_router(cart_router,prefix="/cart")