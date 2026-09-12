from fastapi import FastAPI

from backend.app.api.chat import router as chat_router

app = FastAPI(
    title="MIRA",
    description="Multilingual Intelligent Reasoning Assistant",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "name": "MIRA",
        "status": "Online",
        "message": "MIRA backend is running!"
    }

app.include_router(chat_router)
