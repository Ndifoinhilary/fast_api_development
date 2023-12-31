from fastapi import APIRouter


router = APIRouter(prefix="/blog/post", tags=["blog"])


@router.post("/create")
def create_blog():
    pass
