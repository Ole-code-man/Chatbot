from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status":"ok"}