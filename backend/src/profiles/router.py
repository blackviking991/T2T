#
# Router for all profile related endpoints
#

# Imports
from fastapi import APIRouter, Body, Depends, HTTPException, status, Request
from profiles.models import UserLogin, fake_db, UserInDB, UserSignUp
import profiles.service as profilesService
import profiles.utils as profileUtils
import profiles.auth_handler as authMethods
from profiles.auth_bearer import JWTBearer
import database.database as dbVars


router = APIRouter(
prefix='/profiles',
tags=["Profile Calls"]
)

# Test Router
@router.get("/", tags=["Profile Route"])
def profile_root():
    return {"Message": "Hello! from the Profiles Page"}


## Registration Link
@router.post("/signup", tags=["Register"])
async def create_user(request: Request, user: UserSignUp = Body(...)):
    if dbVars.mongo_db["users"].find_one({"email":user.email}):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Only one account allowed per user email")
    
    # Create a new user
    # todo: Ensure frontend passes password hashed (MD5)
    user_signup = UserInDB(email=user.email, first_name=user.first_name, last_name=user.last_name, roles=user.roles, hashed_password=profileUtils.get_password_hash(user.password))
           
    ##fake_db[str(user.email)] = dict(user_signup)
    dbVars.mongo_db["users"].insert_one(dict(user_signup))
    
    return authMethods.signJWT(user)

# Login Link
@router.post("/login", tags=["Login Page"])
async def user_login(user: UserLogin = Body(...)):
    if profilesService.authenticate_user(dbVars.mongo_db, user.user_name, user.password):
        return {"Message": "Login Successful"}
    return {
        "error": "Wrong login details!"
    }
    
# Locked Test Endpoint
@router.get("/hello", dependencies=[Depends(JWTBearer())], tags=["Auth Check"])
async def auth_check() -> dict:
    return {"Messgae":"You are authenticated"}
    

@router.get("/users/me/")
async def read_users_me(token: str = Depends(JWTBearer())) -> dict:
    payload = authMethods.decodeJWT(token=token)
    return {"payload": payload }
