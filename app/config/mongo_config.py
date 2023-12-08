import motor.motor_asyncio
import certifi
from app.config.logger_config import logger
from app.config.env_config import monogdb_uri, database_name

client = motor.motor_asyncio.AsyncIOMotorClient(monogdb_uri, tlsCAFile=certifi.where())

if client:
    logger.info("MongoDB connection successful.")
else:
    logger.error("MongoDB connection failed.")

database_client = client[database_name]