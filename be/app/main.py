import uvicorn
from fastapi import FastAPI

from db import init_db
from models import *


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
