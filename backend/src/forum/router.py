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
from forum.models import Forum
from forum.utils import forumEntity, forumsEntity, generate_forum_id


router = APIRouter(
prefix='/forum',
tags=["Forum calls"]
)

# Test Router
@router.get("/", tags=["Forum Routes"])
def profile_root():
    return {"Message": "Hello! from the forum Page"}


## Get all forum details
@router.get("/allForums", tags=["All Forums"])
async def view_all_forum():
     allForums = forumsEntity(dbVars.mongo_db[dbConstants.COLLECTION_FORUMS].find())
     if allForums:
         return allForums
     else:
        return {"Messgae":"No Forums found"}
    
      
@router.post("/addForum", tags=["Add Forum"])
async def create_forum(forum: Forum):
    if dbVars.mongo_db[dbConstants.COLLECTION_FORUMS].find_one({"forumName":forum.forumName}):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Duplicate forum names are not allowed")
    
    # create new forum
    forum.fId = generate_forum_id(forum.forumName)
    dbVars.mongo_db[dbConstants.COLLECTION_FORUMS].insert_one(dict(forum))
    myForum = forumEntity(dbVars.mongo_db[dbConstants.COLLECTION_FORUMS].find_one({"forumName":forum.forumName}))
    if myForum:
         return myForum
    else:
        return {"Messgae":"Failed to create a forum"}
    
    