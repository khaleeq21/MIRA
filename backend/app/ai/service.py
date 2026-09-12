from typing import List
from .provider import OpenAIProvider

class AIService:
    def __init__(self, provider: OpenAIProvider):
        self.provider = provider

    def chat(
        self,
        message: str,
        history: List[dict] | None = None,
    ) -> str:
        history = history or []

        conversation = history + [
            {
                "role": "user",
                "content": message,
            }
        ]

        return self.provider.generate_response(conversation)
