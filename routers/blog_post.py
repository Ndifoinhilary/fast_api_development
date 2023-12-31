from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/blog/post", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@router.post("/create")
def create_blog(blog: BlogModel):
    return {"Data": blog}
