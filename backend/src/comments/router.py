#
# Router for all post related endpoints
#

# IMPORTS
import datetime
from fastapi import APIRouter, Body, Depends
from auth.auth_bearer import JWTBearer
from users.models import User
from comments.models import Comment
import auth.auth_handler as authMethods 
import database.constants as dbConstants
import database.database as dbVars
import comments.utils as commentUtils
import comments.service as commentService
import globalUtils as globalUtils

# Router for Posts
router = APIRouter(
prefix='/comments',
tags=["User Comments Call"]
)

#
# Desc: Retrieve a post by post Id
#
@router.get("/get/{comment_id}", tags=["Get Posts"])
async def get_new_post(post_id:str, token:str = Depends(JWTBearer())):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        # todo: Add Role check for the post
        return {"Post": Comment(**dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].find_one({"pID": post_id}))}
    
    return {"Message": "Token Expired, please relogin"}

#
# Desc: Create a new post for a user
#
@router.post("/add", tags=["Create new Comment"])
async def create_new_comment(token:str = Depends(JWTBearer()), newComment: Comment = Body(...)):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        loggedInUser = globalUtils.getLoggedInUser(dict(token_payload).get("user_email"))
        newComment.cID = commentUtils.generate_comment_id()
        newComment.createdBy = loggedInUser.email
        newComment.createdTime =  datetime.datetime.utcnow()
        
        # Update Child Comment Id in the parent comment
        if newComment.parentCommentId:
            commentService.update_parent_comment(newComment.parentCommentId, newComment.cID)
        else:
            commentService.update_post_comment(newComment.postId, newComment.cID)
        
        # Write the comment ID to the user model
        commentService.update_user_comment(newComment.cID, loggedInUser)
        # Write to the db
        print("Writing Comment with ID {} to the DB", newComment.cID)
        dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].insert_one(dict(newComment))
        return {"comment": newComment}
    
    return {"Message": "Token Expired, please relogin"}

#
# Desc: Like a comment
#
@router.get("/like/{commentID}/{isLiked}",  tags=["Update post Likes"])
async def update_like(commentID:str, isLiked:int, token:str = Depends(JWTBearer())):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        loggedInUser = User(**dbVars.mongo_db[dbConstants.COLLECTION_USERS].find_one({"email": dict(token_payload).get("user_email")}))
        createdBy = loggedInUser.email
        
        #likeCount = Post(**dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find_one({}))
        if isLiked == 1:
            dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].update_one({"cID": commentID}, { "$inc": { "likes": +1 }})
            #Update user table with liked comment ids
            commentService.add_comment_like_to_user(createdBy, commentID)
        else:
            dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].update_one({"cID": commentID}, { "$inc": { "likes": -1 }})
            #Update user table by removing liked comment ids
            commentService.remove_comment_like_to_user(createdBy, commentID)
        
        return {"Message": "Comment Like Update done"}
    
    return {"Message": "Token Expired, please relogin"}
