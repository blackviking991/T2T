import jwt
import profiles.constants as profileConstants
import profiles.utils as profileUtils
import time
from typing import Dict
from profiles.models import UserSignUp

def signJWT(user: UserSignUp) -> Dict[str, str]:
    
    payload = {
        "user_id": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "roles": user.roles,
        "expires": time.time() + float(60*profileConstants.ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    token = jwt.encode(payload, profileConstants.JWT_SECRET, algorithm=profileConstants.JWT_ALGORITHM)

    return profileUtils.token_response(token=token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, profileConstants.JWT_SECRET, algorithms=[profileConstants.JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
    