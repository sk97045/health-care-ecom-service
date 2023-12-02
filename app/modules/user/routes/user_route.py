from fastapi import APIRouter, Response, status

from app.modules.user.models.user_model import UserModel, CreateUserModel, UpdateUserModel, UserCollection
from app.modules.user.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get("/", response_model=UserCollection,
            response_description="List all users")
async def get_all_users():
    users = await user_service.get_all_users()
    return UserCollection(users=users)


@router.get("/{userId}", response_model=UserModel,
            response_description="Get a user details")
async def get_user_by_id(userId: str):
    user = await user_service.get_user_by_id(userId)
    return user


@router.post("/", response_model=UserModel, status_code=status.HTTP_201_CREATED,
             response_description="Create a user")
async def create_user(user: CreateUserModel):
    new_user = await user_service.create_user(user)
    return new_user


@router.patch("/{userId}", response_model=UserModel,
              response_description="Update a user details")
async def update_user(userId: str, user: UpdateUserModel):
    updated_user = await user_service.update_user(userId, user)
    return updated_user


@router.delete("/{userId}", response_description="Delete a user")
async def delete_user(userId: str):
    await user_service.delete_user(userId)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
