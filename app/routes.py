from fastapi import APIRouter
from app.modules.cart.cart_route import router as cart_router
from app.modules.user.routes.user_route import router as user_router

router = APIRouter()

router.include_router(cart_router, prefix="/cart")
router.include_router(user_router, prefix="/users", tags=["User"])
