def forumEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "forumName":item["forumName"],
        "fId":item["fId"]
    }
    
def forumsEntity(entity) -> list:
    return [forumEntity(item) for item in entity]
    