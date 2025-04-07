from typing import *

from pydantic import BaseModel


class ChatChatbotRequest(BaseModel):
    """
    Chatbot request schema.
    """

    question: str
    chat_history: List[Dict[str, str]] = []
