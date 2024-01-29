#
# Utility methods for posts
# 

# IMPORTS
import time

# Generating post ID
def generate_comment_id():
    return "c" + str(time.time())[-5:]