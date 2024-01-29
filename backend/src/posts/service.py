#
# Service File to outline services related to posts
#

# Imports
from posts.models import Post
import database.constants as dbConstants
import database.database as dbVars
from comments.models import Comment

# Rendering the child Comments in the main Post
def render_child_comments(mainPost: Post):
    if mainPost.commentIds is not None:
        # I am hoping this is a list
        mainPost.childComments = [Comment(**childComment) for childComment in list(dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].find({"cID": { "$in": mainPost.commentIds}}))]
        
        
# Dynamic Code to populate the child comments into a threaded structure
def render_comment_children(childComments: list[Comment]):
    if childComments == [] or childComments is None:
        return 0
    for childComment in childComments:
        # I am hoping this is a list
        print(childComment)
        childComment.childComments = [Comment(**childComment) for childComment in list(dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].find({"cID": { "$in": childComment.childCommentIds}}))]
        if childComment.childComments is not None:
            if render_comment_children(childComment.childComments) == 0:
                continue
         
    return childComments

def add_post_like_to_user(email:str, postID:str):
    print(email, postID)
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": email}, {"$push":{"likedPostsIds": postID}})