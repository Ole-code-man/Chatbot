from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# paste "uvicorn app.main:app --reload" to run website

app = FastAPI()

class ChatRequest (BaseModel):
    figure: str
    message: str

FIGURE_RESPONSES = {
    "napoleon": "I am Napoleon Bonaparte, Emperor of the French.",
    "cleopatra": "I am Cleopatra, Queen of Egypt.",
    "caesar": "I am Gaius Julius Caesar, dictator of Rome."
}

@app.get("/ping")
def ping():
    return {"status":"ok"}

@app.post("/chat")
def chat(request: ChatRequest):
    figure = request.figure.lower()

    if figure not in FIGURE_RESPONSES:
        raise HTTPException(
            status_code=400,
            detail = f"Unknown historical figure: {request.figure}"
        )
    base_response = FIGURE_RESPONSES[figure]
    return{
        "reply" : f"{base_response} You asked: {request.message}"
    }
