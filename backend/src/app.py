#
# Main Route 
#
from fastapi import FastAPI
from database.database import lifespan
import users.router as profile_router
import forum.router as forum_router

app = FastAPI(lifespan=lifespan)

app.include_router(profile_router.router)
app.include_router(forum_router.router)

@app.get("/home", tags=["Welcome"])
async def read_root():
    return {"message": "Hello World from the T2T app!"}