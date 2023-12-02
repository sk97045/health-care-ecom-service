from fastapi import HTTPException
from app.modules.user.repositories.user_repository import UserRepository
from app.modules.user.types.user import User


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def get_all_users(self):
        users = await self.user_repository.get_all_users()
        return users

    async def get_user_by_id(self, userId: str):
        user = await self.user_repository.get_user_by_id(userId)
        if user is None:
            raise HTTPException(
                status_code=404, detail=f"user {userId} not found")
        return user

    async def create_user(self, user: User):
        newUser = await self.user_repository.create_user(user)
        return newUser

    async def update_user(self, userId: str, user: User):
        updated_user = await self.user_repository.update_user(userId, user)
        if updated_user is None:
            raise HTTPException(
                status_code=404, detail=f"user {userId} not found")
        return updated_user

    async def delete_user(self, userId: str):
        delete_result = await self.user_repository.delete_user(userId)
        if delete_result is 0:
            raise HTTPException(
                status_code=404, detail=f"user {userId} not found")
        return None
