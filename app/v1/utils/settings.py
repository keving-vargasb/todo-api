import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    mongo_uri: str = os.getenv('MONGO_URI')
    mongo_db: str = os.getenv('MONGO_URI')