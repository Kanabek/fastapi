from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    id: int
    title: str
    body: str


posts = [
    {'id':1, 'title': 'New1', 'body': 'Text 1' },
    {'id':2, 'title': 'New2', 'body': 'Text 2' },
    {'id':3, 'title': 'New3', 'body': 'Text 3' },
]


@app.get("/items")
async def items() -> List[Post]:
    return [Post(**post) for post in posts]


@app.get("/items/{id}")
async def items(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/search")
async def search(post_id: Optional[int] = None):
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return post
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return {"data":"No post id provided"}

