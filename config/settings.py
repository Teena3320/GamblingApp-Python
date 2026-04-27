from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")