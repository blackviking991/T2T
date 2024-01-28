
from typing import Optional
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str
    expire_time: str

class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    roles: list
    points: Optional[float] = 0
    # Total comments on the posts by the user
    postCommentCount: Optional[int] = 0
    # Total likes on the comments of the posts by the user
    postCommentLikes: Optional[int] = 0
    # Total likes on the posts by the user
    commentIds: Optional[list]
    # Total Views for all the posts for the user
    postViews: Optional[int] = 0
    interestTags: Optional[list]
    postIds: Optional[list]
    disabled: bool or None = None
    
class UserSignUp(User):
    # encrypted 
    password: str 

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserInDB(User):
    hashed_password: str