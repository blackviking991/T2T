#
# Service File to outline services related to posts
#

# Imports
import database.constants as dbConstants
import database.database as dbVars
from users.models import UserInDB


def update_parent_comment(parentCommentId: str, commentId: str):
    dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].update_one({"cID": parentCommentId}, {"$push":{"childCommentIds": commentId}})

# Updated the commentIds of the parent postid   
def update_post_comment(postId: str, commentId: str):
    dbVars.mongo_db[dbConstants.COLLECTION_POSTS].update_one({"pID": postId}, {"$push":{"commentIds": commentId}})
    
# Update User Model with the CommentIds
def update_user_comment(commentId : str, user: UserInDB):
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": user.email}, {"$push":{"commentIds": commentId}})
    
# Update liked comment ids to the user
def add_comment_like_to_user(email:str, postID:str):
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": email}, {"$push":{"likedCommentsIds": postID}})

# Remove liked comment ids to the user
def remove_comment_like_to_user(email:str, postID:str):
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": email}, {"$pull":{"likedCommentsIds":{postID}}})