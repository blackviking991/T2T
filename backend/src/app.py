#
# Main Route 
#
from fastapi import FastAPI
import profiles.router as profile_router

app = FastAPI()

app.include_router(profile_router.router)

@app.get("/home", tags=["Welcome"])
async def read_root():
    return {"message": "Hello World from the T2T app!"}