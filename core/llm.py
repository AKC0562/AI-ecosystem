from abc import ABC, abstractmethod

from google import genai
from google.genai import types

from config.settings import settings


class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class GeminiLLMProvider(LLMProvider):

    def __init__(self, model: str):
        self.model = model

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
            ),
        )

        return response.text or ""