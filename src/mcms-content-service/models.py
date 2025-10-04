from sqlmodel import SQLModel, Field


class PostBase(SQLModel):
    name: str
    content: str


class Post(PostBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class PostCreate(PostBase):
    pass

