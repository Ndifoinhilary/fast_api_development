from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello():
    return {"Message":"how are you doing "}