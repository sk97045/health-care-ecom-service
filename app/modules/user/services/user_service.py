from fastapi import HTTPException
from app.modules.user.repositories.user_repository import UserRepository
from app.modules.user.types.user import User


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def getAllUsers(self):
        users = await self.user_repository.getAllUsers()
        return users

    async def getUserById(self, userId: str):
        user = await self.user_repository.getUserById(userId)
        if user is None:
            raise HTTPException(
                status_code=404, detail=f"user {userId} not found")
        return user

    async def createUser(self, user: User):
        newUser = await self.user_repository.createUser(user)
        return newUser

    async def updateUser(self, userId: str, user: User):
        updatedUser = await self.user_repository.updateUser(userId, user)
        if updatedUser is None:
            raise HTTPException(
                status_code=404, detail=f"user {userId} not found")
        return updatedUser

    async def deleteUser(self, userId: str):
        deleteResult = await self.user_repository.deleteUser(userId)
        if deleteResult is 0:
            raise HTTPException(
                status_code=404, detail=f"user {userId} not found")
        return None
