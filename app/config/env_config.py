import os
from dotenv import load_dotenv
load_dotenv()

monogdb_uri=os.getenv("MONGODB_URI")
database_name = os.getenv("DATABASE_NAME")