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
        mainPost.childComments = [childComment for childComment in dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].find({"cId": { "$in": mainPost.commentIds}})]
        
        
# Dynamic Code to populate the child comments into a threaded structure
def render_comment_children(childComments: list[Comment]):
    if childComments is None:
        return 0
    for childComment in childComments:
        # I am hoping this is a list
        childComment.childComments = [childComment for childComment in dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].find({"cId": { "$in": childComment.childCommentIds}})]
        if render_comment_children(childComment.childComments) == 0:
             continue
         
    return childComments