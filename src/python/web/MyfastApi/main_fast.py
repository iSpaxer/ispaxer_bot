from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
W    return {"message": "Hello World"}
