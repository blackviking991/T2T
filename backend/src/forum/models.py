
from typing import Optional
from pydantic import BaseModel

class Forum(BaseModel):
    forumName: str
    fID: Optional[str]
    desc: str