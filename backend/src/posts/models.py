from datetime import datetime
from typing import Any
from typing import Optional
from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    # Post ID
    pID: Optional[str]
    title: str
    desc: str
    shortDesc: str
    createdTime: Optional[datetime]
    createdBy: Optional[EmailStr]
    tags: Optional[list] = []
    likes: Optional[int] = 0
    commentIds: Optional[list] = []
    views: Optional[int] = 0
    # Access Levels will only one string ( manager, executive, developer, engineer etc..)
    accessLevel: Optional[str] = ""
    forumName: str
    modifiedDate: Optional[datetime]
    childComments: Optional[Any]
    
class PostLikes(BaseModel):
    pID: str