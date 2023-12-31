from fastapi import FastAPI


app = FastAPI()


@app.get()
async def hello():
    return {"Message":"how are you doing "}