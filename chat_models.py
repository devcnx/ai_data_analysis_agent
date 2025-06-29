from dataclasses import asdict, dataclass
from typing import List, Dict, Literal


@dataclass
class ChatMessage:
    role: Literal['user', 'assistant', 'system']
    content: str


@dataclass
class ChatConversationHistory:
    messages: List[ChatMessage]
    