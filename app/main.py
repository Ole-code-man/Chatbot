from fastapi import FastAPI
from pydantic import BaseModel

# paste "uvicorn app.main:app --reload" to run website

app = FastAPI()

class ChatRequest (BaseModel):
    message: str

@app.get("/ping")
def ping():
    return {"status":"ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    return{
        "reply" : f"You said: {request.message}"
    }
