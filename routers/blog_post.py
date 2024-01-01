from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel
from typing import Dict, Optional, List

router = APIRouter(prefix="/blog/post", tags=["blog"])


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    matedata: Dict[str, str]
    image: Optional[Image] = None


@router.post("/create/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"ID": id, "Data": blog, "version": version}


@router.post("/new/{id}/comment/{coment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None, title="Id of the comment", description="some description", deprecated=True
    ),
    content: str = Body(..., max_length=200),
    v: Optional[List[str]] = Query(None),
    comment_id: int = Path(...),
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "v": v,
        "comment_id": comment_id,
    }
