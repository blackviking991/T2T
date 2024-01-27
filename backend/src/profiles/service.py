#
# Service File to outline JWT Service methods
#

# Imports
from profiles.models import UserInDB
import profiles.utils as profileUtils

def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not profileUtils.verify_password(password, user.hashed_password):
        return False

    return user