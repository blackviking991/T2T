
from typing import Optional
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str
    expire_time: str

class User(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    roles: list
    about: str
    org: list
    points: Optional[float] = 0
    # Total comments on the posts by the user
    postCommentCount: Optional[int] = 0
    # Total likes on the comments of the posts by the user
    postCommentLikes: Optional[int] = 0
    #Total number of views to the post
    postViewCount: Optional[int] = 0
    # Comments by the user
    commentIds: Optional[list] = []
    # Total Views for all the posts for the user
    postViews: Optional[int] = 0
    # Liked posts by the user
    likedPostsIds: Optional[list] = []
    # Liked comments by the user
    likedCommentsIds: Optional[list] = []
    interestTags: Optional[list] = []
    postIds: Optional[list] = []
    viewedPostIds : Optional[list] = []
    disabled: bool or None = None
    
class UserSignUp(User):
    # encrypted 
    password: str 

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserInDB(User):
    hashed_password: str