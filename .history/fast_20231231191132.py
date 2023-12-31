from fastapi import FastAPI, status,Response


app = FastAPI()


@app.get("/")
def hello():
    return {"Message": "how are you doing "}


# working now with status code


@app.get("/blog/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_blog(id: int, response:Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"Message": f"Blog with {id}"}



@app.get('/blog/all', tags=['blog'], summary="Retrieve all blogs", description='to get all the blog in the db')
def get_all_blog():
    return {'Messages' : f'all the blogs in the db '}