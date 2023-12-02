import motor.motor_asyncio
from app.config.logger_config import logger
from app.config.env_config import MONGODB_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)

if client:
    logger.info("MongoDB connection successful.")
else:
    logger.error("MongoDB connection failed.")

vikingsHealthCareDatabase = client["vikings_healthcare"]
