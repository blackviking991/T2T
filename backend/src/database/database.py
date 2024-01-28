from pymongo import MongoClient
from decouple import config
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(">>>>>Loading the Mongo connection <<<<<<")
    global mongodb_client 
    mongodb_client = MongoClient(config("MONGODB_CONNECTION_URL"))
    global mongo_db 
    mongo_db = mongodb_client[config("DB_NAME")]
    print("connected to the database!!")
    yield
    