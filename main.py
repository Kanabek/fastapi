from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home() -> dict[str,str]:
    return {"data":"message"}


@app.get("/contacts")
async def contacts() -> int:
    return 34


posts = [
    {'id':1, 'title': 'New1', 'body': 'Text 1' },
    {'id':2, 'title': 'New2', 'body': 'Text 2' },
    {'id':3, 'title': 'New3', 'body': 'Text 3' },
]


@app.get("/items")
async def get_items() -> list[dict]:
    return posts


@app.get("/items/{id}")
async def get_items_by_id(id: int) -> list[dict]:
    return posts
