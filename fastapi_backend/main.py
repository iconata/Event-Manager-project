from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "FastAPI is running"}

@app.get("/health")
async def health_check():
    return {"message": "OK"}