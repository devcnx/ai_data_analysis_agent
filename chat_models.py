from dataclasses import dataclass
from typing import Literal


@dataclass
class ChatMessage:
    role: Literal['user', 'assistant', 'system']
    content: str


@dataclass
class ChatConversationHistory:
    messages: list[ChatMessage]
    
