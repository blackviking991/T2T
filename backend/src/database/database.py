from pymongo import MongoClient
import database.constants as dbConstants
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(">>>>>Loading the Mongo connection <<<<<<")
    global mongodb_client 
    mongodb_client = MongoClient(dbConstants.MONGODB_CONNECTION_URL)
    global mongo_db 
    mongo_db = mongodb_client[dbConstants.MONGO_DB_NAME]
    print("connected to the database!!")
    yield
    