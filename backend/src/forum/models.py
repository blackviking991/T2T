
from typing import Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    expire_time: str

class Forum(BaseModel):
    forumName: str
    fId: str
    desc: str