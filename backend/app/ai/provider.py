# pyrefly: ignore [missing-import]
from openai import OpenAI
from typing import List
class OpenAIProvider:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, message: List[dict]) ->str:
        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input=message,
        )

        return response.output_text