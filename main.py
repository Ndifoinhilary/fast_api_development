from fastapi import FastAPI
from routers import blog_post, blog_get
from db import models
from db.database import engine

app = FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
def hello():
    return {"Messages": "Testing this shirt stuff"}


models.Base.metadata.create_all(engine)
