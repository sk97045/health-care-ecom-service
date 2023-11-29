class MongoDbUtil:
    def __init__(self, model):
        self.model = model
    
    async def createDocument(self,document):
        result = await self.model.insert_one(document)
        return result
        
    async def readDocument(self,filter):
       result = await self.model.find_one(filter);
       if result is not None and "_id" in result:
        result["_id"] = str(result["_id"])
       return result;
   
    async def getDocuments(self,filter,pageSize: int | None):
       documents = await self.model.find(filter).to_list(pageSize);
       if len(documents) != 0:
        for document in documents:
            document["_id"] = str(document.pop("_id"))
       return documents;

    async def updateDocument(self,filter,updateQuery):
        result = await self.model.update_one(filter,updateQuery)
        return result