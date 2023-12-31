from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/blog/post", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@router.post("/create/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"ID": id, "Data": blog, "version": version}


@router.post("/new/{id}/comment")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_id: int = Query(
        None, title="Id of the comment", description="some description", deprecated=True
    ),
):
    return {"blog": blog, "id": id, "comment_id": comment_id}
