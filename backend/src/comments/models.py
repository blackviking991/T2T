from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, EmailStr


class Comment(BaseModel):
    # Post ID
    cID: Optional[str]
    text: str
    createdTime: Optional[datetime]
    createdBy: Optional[EmailStr]
    postId: str
    likes: Optional[int]
    parentCommentId: Optional[str]
    childCommentIds: Optional[list]
    childComments: Optional[Any]