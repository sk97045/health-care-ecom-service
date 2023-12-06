from fastapi import APIRouter
from app.routes.cart_route import router as cart_router
from app.routes.product_route import router as product_router

router = APIRouter()

router.include_router(cart_router,prefix="/cart")  
router.include_router(product_router,prefix="/product")