from fastapi import FastAPI, Depends
from sqlmodel import select
from sqlmodel import Session
from .db import get_session, init_db
from .models import Post, PostCreate

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts", response_model=list[Post])
def get_posts(session: Session = Depends(get_session)):
    result = session.execute(select(Post))
    posts = result.scalars().all()

    return [Post(name=post.name, content=post.content, id=post.id) for post in posts]


@app.post("/posts")
def add_post(post: PostCreate, session: Session = Depends(get_session)):
    post = Post(name=post.name, content=post.content)
    session.add(post)
    session.commit()
    session.refresh(post)

    return post

