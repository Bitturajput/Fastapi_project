from pydantic import  BaseModel
from fastapi import Fastapi

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

