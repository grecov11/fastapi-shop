from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def hello_index():
    return {"Message": "Hello index!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
