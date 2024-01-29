#
# Router for all profile related endpoints
#

# Imports
from fastapi import APIRouter, Body, Depends, HTTPException, status, Request
from users.models import UserLogin, UserInDB, UserSignUp, User
import users.service as usersService
import users.utils as profileUtils
import auth.auth_handler as authMethods
from auth.auth_bearer import JWTBearer
import database.database as dbVars
import database.constants as dbConstants


router = APIRouter(
prefix='/users',
tags=["Users Registration Calls"]
)

# Test Router
@router.get("/", tags=["Users Route"])
def profile_root():
    return {"Message": "Hello! from the users Page"}


## Registration Link
@router.post("/signup", tags=["Register"])
async def create_user(user: UserSignUp = Body(...)):
    if dbVars.mongo_db[dbConstants.COLLECTION_USERS].find_one({"email":user.email}):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Only one account allowed per user email")
    
    # Create a new user
    # todo: Ensure frontend passes password hashed (MD5)
    user_signup = UserInDB(email=user.email, firstName=user.firstName, lastName=user.lastName, roles=user.roles, about=user.about, org=user.org, hashed_password=profileUtils.get_password_hash(user.password))
           
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].insert_one(dict(user_signup))
    
    return authMethods.signJWT(user)

# Login Link
@router.post("/login", tags=["Login Page"])
async def user_login(user: UserLogin = Body(...)):
    if usersService.authenticate_user(dbVars.mongo_db, user.email, user.password):
        login_token = authMethods.signJWT(user)
        return {"Message": "Login Successful", "access_token": dict(login_token).get('access_token')}
    return {
        "error": "Wrong login details!"
    }
    
# Locked Test Endpoint
@router.get("/hello", dependencies=[Depends(JWTBearer())], tags=["Auth Check"])
async def auth_check() -> dict:
    return {"Messgae":"You are authenticated"}
    

@router.get("/me/")
async def read_users_me(token: str = Depends(JWTBearer())) -> dict:
    payload = authMethods.decodeJWT(token=token)
    loggedInUser = User(**dbVars.mongo_db[dbConstants.COLLECTION_USERS].find_one({"email": dict(payload).get("user_email")}))
    usersService.recalculate_user_points(loggedInUser)
    return {"payload": payload, "user": loggedInUser}
