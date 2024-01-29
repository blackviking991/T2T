
# Imports
from models import UserRoles
from decouple import config


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


# Weights for the gamification algorithm
USER_COMMENT_LIKES_WEIGHT = config("COMMENT_LIKES_WEIGHT")
USER_COMMENT_COUNT_WEIGHT = config("COMMENTS_COUNT_WEIGHT")
USER_POSTS_COUNTS_WEIGHT = config("POSTS_COUNT_WEIGHT")
USER_POSTS_LIKES_WEIGHT = config("POSTS_LIKES_WEIGHT")
USER_POSTS_VIEWS_WEIGHT = config("POSTS_VIEW_WEIGHT")
