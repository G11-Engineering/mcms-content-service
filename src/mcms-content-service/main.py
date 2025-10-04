from fastapi import FastAPI
from .db import init_db
from .models import Post

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}
