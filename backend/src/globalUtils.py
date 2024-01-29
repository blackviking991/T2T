from users.models import User
import database.constants as dbConstants
import database.database as dbVars

# Return Logged in User
def getLoggedInUser(email:str):
    return User(**dbVars.mongo_db[dbConstants.COLLECTION_USERS].find_one({"email": email}))