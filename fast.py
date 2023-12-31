from typing import Optional
from fastapi import FastAPI, status, Response
from routers import blog_get

app = FastAPI()

app.include_router(blog_get.router)


@app.get("/")
def hello():
    return {"Messages": "Testing this shirt stuff"}
