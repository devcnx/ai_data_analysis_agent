import time

from rich.console import Console

from chat_models import ChatConversationHistory
from config import DEFAULT_MODEL
from ollama_client import OllamaClient
from rick.markdown import Markdown

class ChatManager:
    client: OllamaClient = None
    model: str = DEFAULT_MODEL
    history: ChatConversationHistory = ChatConversationHistory()
    console: Console = Console()