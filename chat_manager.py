from rich.console import Console
from typing import final

from chat_models import ChatConversationHistory
from config import DEFAULT_MODEL
from ollama_client import OllamaClient


@final
class ChatManager:
    client: OllamaClient | None
    model: str
    console: Console
    history: ChatConversationHistory

    def __init__(self, model: str = DEFAULT_MODEL):
        self.client: OllamaClient | None = None
        self.model = model
        self.history = ChatConversationHistory(messages=[])
        self.console = Console()