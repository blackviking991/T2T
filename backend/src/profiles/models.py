
from pydantic import BaseModel, EmailStr
from models import UserRoles  

# Fake DB to test JWT Auth
# Manager login pw is manager1234
# Developer login pw is dev1234
fake_db = {
    "manager@ti.com": {
        "first_name": "manager_firstname",
        "last_name": "manager_lastname",
        "email": "manager@ti.com",
        "roles": [UserRoles.MANAGER, UserRoles.DEVELOPER],
        "hashed_password": "$2b$12$v8dDblcwQ1JWh6BXsNbvJOpOvIAkkzPouLncrFL35BjXYdXPKKGmG",
        "disabled": False
    },
    "developer@ti.com": {
        "first_name": "developer_firstname",
        "last_name": "developer_lastname",
        "email": "developer@ti.com",
        "roles": [UserRoles.DEVELOPER],
        "hashed_password": "$2b$12$0uBWxjQkvUTd7bHI7EymZekurWkMs70nHFmwBYRGR9KTREBct9MJC",
        "disabled": False
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str
    expire_time: str

class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    roles: list
    disabled: bool or None = None
    
class UserSignUp(User):
    # encrypted 
    password: str 

class UserLogin(BaseModel):
    user_name: str
    password: str

class UserInDB(User):
    hashed_password: str