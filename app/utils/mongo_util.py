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
   
    async def updateDocument(self,filter,updateQuery):
        result = await self.model.update_one(filter,updateQuery)
        return result