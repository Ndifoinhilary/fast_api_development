from fastapi import FastAPI, status


app = FastAPI()


@app.get("/")
def hello():
    return {"Message": "how are you doing "}


# working now with status code


@app.get("/blog/{id}", status_code=404)
def get_blog(id: int):
    if id > 5:
        return {"Error": f"Blog {id} not found"}
    else:
        return {"Message": f"Blog with {id}"}
