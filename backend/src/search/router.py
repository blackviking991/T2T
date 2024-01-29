#
# Router for all profile related endpoints
#

# Imports
from fastapi import APIRouter, Body, Depends, HTTPException, status, Request
from fuzzysearch import find_near_matches
import math
from comments.models import Comment
from posts.models import Post
import database.database as dbVars
import database.constants as dbConstants


router = APIRouter(
prefix='/search',
tags=["Search Engine"]
)


## Main Search endpoint
@router.get("/{searchString}", tags=["search field"])
async def retrieve_linked_posts(searchString:str):
    max_deletions = math.floor(len(searchString)*0.4)
    max__l_dist = 1
    max_insertions = math.floor(len(searchString)*0.2)
    
    ## Get all post ids for which the comments threw a match
    positive_post_ids_comments_raw = [Comment(**comment).postId if len(find_near_matches(searchString, Comment(**comment).text, max_l_dist=max__l_dist, max_deletions=max_deletions, max_insertions=max_insertions)) > 0 else "0" for comment in list(dbVars.mongo_db[dbConstants.COLLECTION_COMMENTS].find())]
    positive_post_ids_comments_filtered = [id for id in positive_post_ids_comments_raw if id != "0"]
    ## Get all post ids for which the title and description threw a match
    positive_post_ids_posts_raw = [Post(**post).pID if len(find_near_matches(searchString, Post(**post).desc + Post(**post).title + Post(**post).shortDesc, max_l_dist=max__l_dist, max_deletions=max_deletions, max_insertions=max_insertions)) > 0 else "0" for post in list(dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find())]
    positive_post_ids_posts_filtered = [id for id in positive_post_ids_posts_raw if id != "0"]
    
    final_postids = positive_post_ids_posts_filtered + [postids for postids in positive_post_ids_comments_filtered if postids not in positive_post_ids_posts_filtered]
    
    return {"search": [Post(**searchPosts) for searchPosts in list(dbVars.mongo_db[dbConstants.COLLECTION_POSTS].find({"pID":{"$in": final_postids}}))]}
    
