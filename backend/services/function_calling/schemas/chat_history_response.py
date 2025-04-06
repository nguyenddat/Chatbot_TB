from typing import *

from pydantic import BaseModel

class ChatHistoryResponse(BaseModel):
    question: str
    response: str