from datetime import datetime
from typing import Any
from typing import Optional
from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    # Post ID
    pID: Optional[str]
    title: str
    desc: str
    createdTime: Optional[datetime]
    createdBy: Optional[EmailStr]
    tags: Optional[list]
    likes: Optional[int]
    commentIds: Optional[list[str]]
    views: Optional[int]
    forumName: str
    modifiedDate: Optional[datetime]
    childComments: Optional[Any]
    
    