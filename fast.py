from fastapi import FastAPI
from routers import blog_post, blog_get

app = FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
def hello():
    return {"Messages": "Testing this shirt stuff"}
