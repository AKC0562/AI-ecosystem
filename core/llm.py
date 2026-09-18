from abc import ABC, abstractmethod

class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
class MockLLMProvider(LLMProvider):

    def generate(self, prompt: str) -> str:
        return f"AI received: {prompt}"