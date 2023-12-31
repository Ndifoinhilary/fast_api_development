from typing import Optional
from fastapi import FastAPI, status, Response, APIRouter


router = APIRouter(prefix="/blog", tags=["blog"])


# working now with status code


@router.get("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"Message": f"Blog with {id}"}


# how to add tags,  summary and description in fastapi
@router.get(
    "/all",
    summary="Retrieve all blogs",
    description="to get all the blog in the db",
)
def get_all_blog(page=1, page_size: Optional[int] = None):
    return {"Message": f"{page} in the blog of size {page_size}"}
