from pymongo import MongoClient
from fastapi import Depends
from app.v1.utils.settings import Settings

settings = Settings()

MONGO_URI = settings.mongo_uri
MONGO_DB = settings.mongo_db

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]