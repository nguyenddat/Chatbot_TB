from typing import *

from pydantic import BaseModel

class ChatHistoryResponse(BaseModel):
    quesion: str
    response: str