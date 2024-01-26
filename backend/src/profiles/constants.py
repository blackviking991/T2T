# 
# Constants for Auth
# 

# Imports
from decouple import config

#JWT Constants
JWT_SECRET = config("secret_key")
JWT_ALGORITHM = config("algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = config("token_expire_time")