from bson import ObjectId
from pymongo import ReturnDocument

from app.config.mongo_config import vikingsHealthCareDatabase
from app.modules.user.types.user import User
from app.utils.rename_document_id import renameDocumentId


class UserRepository:
    def __init__(self):
        self.user_collection = vikingsHealthCareDatabase.get_collection(
            'users')

    async def getAllUsers(self):
        users = await self.user_collection.find().to_list(None)
        return renameDocumentId(users)

    async def getUserById(self, userId: str):
        user = await self.user_collection.find_one({"_id": ObjectId(userId)})
        print(user)
        return renameDocumentId(user)

    async def createUser(self, user: User):
        print(user, dict(user))
        createResult = await self.user_collection.insert_one(dict(user))
        newUser = await self.user_collection.find_one({"_id": createResult.inserted_id})
        return renameDocumentId(newUser)

    async def updateUser(self, userId: str, user: User):
        updateResult = await self.user_collection.find_one_and_update(
            {"_id": ObjectId(userId)},
            {"$set": dict(user)},
            return_document=ReturnDocument.AFTER
        )
        return renameDocumentId(updateResult)

    async def deleteUser(self, userId: str):
        deleteResult = await self.user_collection.delete_one({"_id": ObjectId(userId)})
        return deleteResult.deleted_count
