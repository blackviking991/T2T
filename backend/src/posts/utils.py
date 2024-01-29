#
# Utility methods for posts
# 

# IMPORTS
import time

# Generating post ID
def generate_post_id(title: str):
    return "p" + str(time.time())[-5:]

# Enforcing tags to be lowercase
def make_tags_lowerCase(taglist: list):
    return [tag.lower() for tag in taglist]