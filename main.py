import json
from bson import json_util
from fastapi import FastAPI
from app.v1.utils.db import db

app = FastAPI()

@app.get('/')
def home():
    collection = db['riders']
    data = collection.find({})
    return json.loads(json_util.dumps(data))