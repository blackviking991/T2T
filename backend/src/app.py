#
# Main Route 
#
from fastapi import FastAPI
from database.database import lifespan
import users.router as profileRouter
import posts.router as postRouter
import forum.router as forumRouter
import comments.router as commentRouter
import search.router as searchRouter

app = FastAPI(lifespan=lifespan)

app.include_router(profileRouter.router)
app.include_router(postRouter.router)
app.include_router(forumRouter.router)
app.include_router(commentRouter.router)
app.include_router(searchRouter.router)


@app.get("/home", tags=["Welcome"])
async def read_root():
    return {"message": "Hello World from the T2T app!"}