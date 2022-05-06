from fastapi import FastAPI
from mangum import Mangum
version = "v0.0.1"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello There!"}

handler = Mangum(app)