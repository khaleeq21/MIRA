import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.ai.provider import OpenAIProvider
from backend.app.ai.service import AIService
from backend.app.services.memory import ConversationMemory


PROJECT_ROOT = Path(__file__).resolve().parents[3]
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_FILE)


router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    conversation_id: str = "default"


class ChatResponse(BaseModel):
    response: str
    conversation_id: str


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError(
        f"OPENAI_API_KEY is not configured. Expected .env at: {ENV_FILE}"
    )


provider = OpenAIProvider(api_key)
ai_service = AIService(provider)
memory = ConversationMemory()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    history = memory.get_history(request.conversation_id)

    response = ai_service.chat(
        message=request.message,
        history=history,
    )

    memory.add_message(
        request.conversation_id,
        "user",
        request.message,
    )

    memory.add_message(
        request.conversation_id,
        "assistant",
        response,
    )

    return ChatResponse(
        response=response,
        conversation_id=request.conversation_id,
    )
