from fastapi import APIRouter, Depends

from database.base import get_db
from schemas import (
    chatbot
)
from services.function_calling import function_calling

router = APIRouter()

@router.post("/chatbot")
def chat_chatbot(data: chatbot.ChatChatbotRequest, db = Depends(get_db)):
    question = data.question

    response = function_calling.function_calling(question = question, db = db)
    return response