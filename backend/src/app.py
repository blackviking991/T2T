#
# Main Route 
#
from fastapi import FastAPI
from database.database import lifespan
import users.router as profileRouter
import posts.router as postRouter
import forum.router as forum_router

app = FastAPI(lifespan=lifespan)

app.include_router(profileRouter.router)
app.include_router(postRouter.router)
app.include_router(forum_router.router)


@app.get("/home", tags=["Welcome"])
async def read_root():
    return {"message": "Hello World from the T2T app!"}