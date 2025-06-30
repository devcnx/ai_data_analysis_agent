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
        """
        Initialize a new ChatManager instance with the specified model, an empty conversation history, and a console for output.
        
        Parameters:
            model (str): The name of the model to use for chat interactions. Defaults to the configured default model.
        """
        self.client: OllamaClient | None = None
        self.model = model
        self.history = ChatConversationHistory(messages=[])
        self.console = Console()