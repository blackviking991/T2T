#
# Service File to outline services related to posts
#

# Imports
from posts.models import Post
import database.constants as dbConstants
import database.database as dbVars
from comments.models import Comment
import posts.constants as postConstants

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

# Update liked post ids with the new ones
def add_post_like_to_user(email:str, postID:str, action:int):
    print(email, postID)
    if action == 1:
        dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": email}, {"$push":{"likedPostsIds": postID}})
    elif action == 0:
        dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": email}, {"$pull":{"likedPostsIds": postID}})

# logic to update for each view of the post    
def add_post_view_count(email:str, postID:str):
    #Increase the post view count by one
    dbVars.mongo_db[dbConstants.COLLECTION_POSTS].update_one({"pID": postID}, { "$inc": { "views": +1 }})
    # increase the user table with post view count
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": email}, {"$inc": {"postViewCount": +1}})
    # update the user table with viewed post IDs
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": email}, {"$addToSet": {"viewedPostIds": postID}})
    
def add_post_ids_to_user(email:str, postID:str):
    print(email, postID)
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": email}, {"$push":{"postIds": postID}})

#Get is liked value for a user Post
def get_is_liked_for_post(likedPostIds: list, postId: str):
    return 1 if postId in list(likedPostIds) else 0
    
# Get access Level for a new post
def get_access_level_for_post(userAccessLevel: list):
    numeric_access_list_min_value = min([postConstants.POST_ACCESS_LEVEL_DICT.get(x) for x in userAccessLevel])
    if numeric_access_list_min_value is None: 
        numeric_access_list_min_value = 0
    
    return [key for key in postConstants.POST_ACCESS_LEVEL_DICT.keys() if postConstants.POST_ACCESS_LEVEL_DICT.get(key) ==numeric_access_list_min_value ]
    
    