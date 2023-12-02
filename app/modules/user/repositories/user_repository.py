from bson import ObjectId
from pymongo import ReturnDocument

from app.config.mongo_config import vikingsHealthCareDatabase
from app.modules.user.types.user import User
from app.utils.rename_document_id import rename_document_id


class UserRepository:
    def __init__(self):
        self.user_collection = vikingsHealthCareDatabase.get_collection(
            'users')

    async def get_all_users(self):
        users = await self.user_collection.find().to_list(None)
        return rename_document_id(users)

    async def get_user_by_id(self, userId: str):
        user = await self.user_collection.find_one({"_id": ObjectId(userId)})
        return rename_document_id(user)

    async def create_user(self, user: User):
        create_result = await self.user_collection.insert_one(user)
        new_user = await self.user_collection.find_one({"_id": create_result.inserted_id})
        return rename_document_id(new_user)

    async def update_user(self, userId: str, user: User):
        update_result = await self.user_collection.find_one_and_update(
            {"_id": ObjectId(userId)},
            {"$set": dict(user)},
            return_document=ReturnDocument.AFTER
        )
        return rename_document_id(update_result)

    async def delete_user(self, userId: str):
        delete_result = await self.user_collection.delete_one({"_id": ObjectId(userId)})
        return delete_result.deleted_count
