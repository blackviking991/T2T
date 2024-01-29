
from typing import Optional
from pydantic import BaseModel

class Forum(BaseModel):
    forumName: str
    fId: Optional[str]
    desc: str