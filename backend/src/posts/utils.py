#
# Utility methods for posts
# 

# IMPORTS
import random

# Generating post ID
def generate_post_id(title: str):
    return "p" + title[0] + title[-1] + str(random.randint(00000,99999))

# Enforcing tags to be lowercase
def make_tags_lowerCase(taglist: list):
    return [tag.lower() for tag in taglist]