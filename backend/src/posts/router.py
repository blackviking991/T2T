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
import posts.service as postService
import globalUtils as globalUtils

# Router for Posts
router = APIRouter(
prefix='/posts',
tags=["User Posts Call"]
)

#
# Desc: Retrieve a post by post Id
#
@router.get("/get/{post_id}", tags=["Get Posts"])
async def get_new_post(post_id:str, token:str = Depends(JWTBearer())):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        loggedInUser = globalUtils.getLoggedInUser(dict(token_payload).get("user_email"))
        # todo: Add Role check for the post
        postDb = Post(**dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find_one({"pID": post_id}))
        
        # Render Level 1 of comments
        postService.render_child_comments(postDb)
        
        print(postDb)
        
        # Dynamically render Level 2 of comments
        postDb.childComments = postService.render_comment_children(postDb.childComments)
        email = loggedInUser.email
        print(email,post_id)
        postService.add_post_view_count(email, post_id)
        return {"post": postDb}
    
    return {"Message": "Token Expired, please relogin"}

#
# Desc: Retrieve a post by post Id
#
@router.get("/getUserPosts", tags=["Get All Posts for User"])
async def get_user_posts(token:str = Depends(JWTBearer())):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        # todo: Add Role check for the post
        postsList = [Post(**post) for post in list(dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find({"createdBy": dict(token_payload).get("user_email")}))]
        
        return {"posts": postsList}
    
    return {"Message": "Token Expired, please relogin"}


## Get all posts of a forum
@router.get("/getForumPosts/{forumName}", tags=["Get One Forums posts"])
async def get_forum_posts(forumName:str, token:str = Depends(JWTBearer())):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        return {"posts": [Post(**post) for post in list(dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find({"forumName":forumName}))]}
        #else:
            #return {"Messgae":"No Forums found"}
        
    return {"Message": "Token Expired, please relogin"}
#
# Desc: Create a new post for a user
#
@router.post("/add", tags=["Create new Post"])
async def create_new_post(token:str = Depends(JWTBearer()), newPost: Post = Body(...)):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        loggedInUser = globalUtils.getLoggedInUser(dict(token_payload).get("user_email"))
        newPost.pID = postUtils.generate_post_id(newPost.title)
        newPost.createdBy = loggedInUser.email
        newPost.createdTime = newPost.modifiedDate = datetime.datetime.utcnow()
        newPost.tags = postUtils.make_tags_lowerCase(newPost.tags if newPost.tags is not None else [])
        
        # Write to the db
        print("Writing Post with ID {} to the DB", newPost.pID)
        dbVars.mongo_db[dbConstants.COLLECTION_POSTS].insert_one(dict(newPost))
        postService.add_post_ids_to_user(loggedInUser.email, newPost.pID)
        return {"Message": "Post Successfully added"}
    
    return {"Message": "Token Expired, please relogin"}

#
# Desc: Like a post
#
@router.get("/like/{postID}",  tags=["Update post Likes"])
async def update_like(postID:str, token:str = Depends(JWTBearer())):
    token_payload = authMethods.decodeJWT(token=token)
    if token_payload is not None:
        loggedInUser = User(**dbVars.mongo_db[dbConstants.COLLECTION_USERS].find_one({"email": dict(token_payload).get("user_email")}))
        createdBy = loggedInUser.email
        
        #likeCount = Post(**dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find_one({}))
        print("================ postID")
        print(postID)
        print(createdBy)
        dbVars.mongo_db[dbConstants.COLLECTION_POSTS].update_one({"pID": postID}, { "$inc": { "likes": +1 }})
        postService.add_post_like_to_user(createdBy, postID)
        return {"Message": "Like Successfully added"}
    
    return {"Message": "Token Expired, please relogin"}