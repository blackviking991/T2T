#
# Service File to outline JWT Service methods
#

# Imports
from users.models import UserInDB
import users.utils as profileUtils
import database.constants as dbConstants

def get_user(db, username: str):
    if db[dbConstants.COLLECTION_USERS].find_one({"email":username}):
        user_data = db[dbConstants.COLLECTION_USERS].find_one({"email":username})
        return UserInDB(**user_data)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not profileUtils.verify_password(password, user.hashed_password):
        return False

    return user