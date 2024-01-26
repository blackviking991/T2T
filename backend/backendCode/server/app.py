from fastapi import FastAPI

app = FastAPI()


@app.get("/home", tags=["Welcome"])
async def read_root():
    return {"message": "Hello World from the T2T app!"}