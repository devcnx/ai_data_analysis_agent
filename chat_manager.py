import time

from rich.console import Console

from chat_models import ChatConversationHistory
from config import DEFAULT_MODEL
from ollama_client import OllamaClient
from rich.markdown import Markdown

class ChatManager:
    client: OllamaClient | None
    model: str

    def __init__(self, model: str = DEFAULT_MODEL):
        self.client: OllamaClient | None = None
        self.model = model
        self.history = ChatConversationHistory()
        self.console = Console()