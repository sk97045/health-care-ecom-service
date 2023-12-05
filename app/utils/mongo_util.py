from pymongo import ReturnDocument

from app.utils.document_id_helper import rename_document_id

class MongoDbUtil:
    def __init__(self, model):
        self.model = model
    
    async def create_document(self,document):
        create_result = await self.model.insert_one(document)
        created_document = await self.model.find_one(
            {"_id": create_result.inserted_id})
        return rename_document_id(created_document)
        
    async def read_document(self,filterQuery):
        result = await self.model.find_one(filterQuery)
        return rename_document_id(result)
   
    async def fetch_documents(self,filter,pageSize: int | None):
       documents = await self.model.find(filter).to_list(pageSize)
       return rename_document_id(documents)

    async def update_document(self,filterQuery,updateQuery):
        result = await self.model.find_one_and_update(
            filterQuery,
            updateQuery, 
            return_document=ReturnDocument.AFTER)
        return rename_document_id(result)
    
    async def delete_document(self, filter):
        result = await self.model.delete_one(filter)
        return result.deleted_count