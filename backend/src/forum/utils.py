#
# Utility methods for forum
# 

# IMPORTS
import random

# Generating forum ID
def generate_forum_id(title: str):
    return "f" + title[0] + title[-1] + str(random.randint(00000,99999))


def forumEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "forumName":item["forumName"],
        "fID":item["fID"]
    }
    
def forumsEntity(entity) -> list:
    return [forumEntity(item) for item in entity]