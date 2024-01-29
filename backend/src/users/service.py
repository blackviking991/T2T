#
# Service File to outline JWT Service methods
#

# Imports
from users.models import UserInDB
import users.utils as profileUtils
import database.constants as dbConstants
import database.database as dbVars
import users.constants as userConstants
from comments.models import Comment
from posts.models import Post

def get_user(db, username: str):
    if db[dbConstants.COLLECTION_USERS].find_one({"email":username}):
        user_data = db[dbConstants.COLLECTION_USERS].find_one({"email":username})
        return UserInDB(**user_data)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not profileUtils.verify_password(password, user.hashed_password):
        return False

    return user


# Main Service Method to recalculate Points ( gamification )
def recalculate_user_points(user: UserInDB):
    ## User Score for number of comments
    user_comment_count_score = float(userConstants.USER_COMMENT_COUNT_WEIGHT) * float(len(user.commentIds))
    print(user_comment_count_score)
    
    ## Comment Likes Score
    user_comment_likes_score = float(userConstants.USER_COMMENT_LIKES_WEIGHT) * float(sum([Comment(**childComment).likes for childComment in list(dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].find({"cID": { "$in": user.commentIds}}))]))
    print(user_comment_likes_score)
    
    ## User Post Counts weight
    user_post_count_score =  float(userConstants.USER_POSTS_COUNTS_WEIGHT) * float(len(user.postIds))
    print(user_post_count_score)
    
    ## Post Likes Score
    user_post_likes_score = float(userConstants.USER_POSTS_LIKES_WEIGHT) * float(sum([Post(**posts).likes for posts in list(dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find({"pID": { "$in": user.postIds}}))]))
    print(user_post_likes_score)
    
    ## Post Likes Score
    user_post_views_score = float(userConstants.USER_POSTS_VIEWS_WEIGHT) * float(sum([Post(**posts).views for posts in list(dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find({"pID": { "$in": user.postIds}}))]))
    print(user_post_views_score)
    
    user_total_score = sum([user_comment_count_score, user_comment_likes_score, user_post_count_score, user_post_likes_score, user_post_views_score]) / 23
    
    dbVars.mongo_db[dbConstants.COLLECTION_USERS].update_one({"email": user.email}, {"$set":{"points": user_total_score}})