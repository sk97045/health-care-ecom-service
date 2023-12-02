from fastapi import APIRouter, Response, status

from app.modules.user.models.user_model import UserModel, CreateUserModel, UpdateUserModel, UserCollection
from app.modules.user.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get("/", response_model=UserCollection,
            response_description="List all users")
async def getAllUsers():
    users = await user_service.getAllUsers()
    return UserCollection(users=users)


@router.get("/{userId}", response_model=UserModel,
            response_description="Get a user details")
async def getUserById(userId: str):
    user = await user_service.getUserById(userId)
    return user


@router.post("/", response_model=UserModel, status_code=status.HTTP_201_CREATED,
             response_description="Create a user")
async def createUser(user: CreateUserModel):
    newUser = await user_service.createUser(user)
    return newUser


@router.patch("/{userId}", response_model=UserModel,
              response_description="Update a user details")
async def updateUser(userId: str, user: UpdateUserModel):
    updatedUser = await user_service.updateUser(userId, user)
    return updatedUser


@router.delete("/{userId}", response_description="Delete a user")
async def deleteUser(userId: str):
    await user_service.deleteUser(userId)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
