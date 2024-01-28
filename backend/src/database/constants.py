# Constants for database
from decouple import config

MONGODB_CONNECTION_URL = config("MONGODB_CONNECTION_URL")
MONGO_DB_NAME = config("DB_NAME")

# Collection Names
COLLECTION_USERS = "users"
COLLECTION_FORUMS = "forums"