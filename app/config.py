import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
DB_URL = os.getenv("DB_URL")
REDIS_URL = os.getenv("REDIS_URL")
