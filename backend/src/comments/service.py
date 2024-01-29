#
# Service File to outline services related to posts
#

# Imports
import database.constants as dbConstants
import database.database as dbVars


def update_parent_comment(parentCommentId: str, commentId: str):
    dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].update_one({"cID": parentCommentId}, {"$push":{"childCommentIds": commentId}})

# Updated the commentIds of the parent postid   
def update_post_comment(postId: str, commentId: str):
    dbVars.mongo_db[dbConstants.COLLECTION_POSTS].update_one({"pID": postId}, {"$push":{"commentIds": commentId}})