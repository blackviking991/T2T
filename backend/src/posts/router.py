#
# Router for all post related endpoints
#

# IMPORTS
import datetime
from fastapi import APIRouter, Body, Depends
from auth.auth_bearer import JWTBearer
from users.models import User
from posts.models import Post
import auth.auth_handler as authMethods 
import database.constants as dbConstants
import database.database as dbVars
import posts.utils as postUtils

# Router for Posts
router = APIRouter(
prefix='/posts',
tags=["User Posts Call"]
)

#
# Desc: Retrieve a post by post Id
#
@router.get("/get/{post_id}", tags=["Get Posts"])
async def create_new_post(post_id:str, token:str = Depends(JWTBearer())):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        # todo: Add Role check for the post
        return {"Post": Post(**dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find_one({"pID": post_id}))}
    
    return {"Message": "Token Expired, please relogin"}

#
# Desc: Create a new post for a user
#
@router.post("/add", tags=["Create new Post"])
async def create_new_post(token:str = Depends(JWTBearer()), newPost: Post = Body(...)):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        loggedInUser = User(**dbVars.mongo_db[dbConstants.COLLECTION_USERS].find_one({"email": dict(token_payload).get("user_email")}))
        newPost.pID = postUtils.generate_post_id(newPost.title)
        newPost.createdBy = loggedInUser.email
        newPost.createdTime = newPost.modifiedDate = datetime.datetime.utcnow()
        newPost.tags = postUtils.make_tags_lowerCase(newPost.tags if newPost.tags is not None else [])
        
        # Write to the db
        print("Writing Post with ID {} to the DB", newPost.pID)
        dbVars.mongo_db[dbConstants.COLLECTION_POSTS].insert_one(dict(newPost))
        return {"Message": "Post Successfully added"}
    
    return {"Message": "Token Expired, please relogin"}