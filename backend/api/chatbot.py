from fastapi import APIRouter, Depends

from database.base import get_db
from schemas import (
    chatbot
)
from services.function_calling import function_calling
from services.function_calling.core import chat_history

router = APIRouter()

@router.post("/chatbot")
def chat_chatbot(data: chatbot.ChatChatbotRequest, db = Depends(get_db)):
    question = data.question

    response = function_calling.function_calling(question = question, db = db)
    chat_history.chat_history_mananger.add_chat(
        question = question,
        response = str(response)
    )

    return {
        "result": "successfully",
        "status": 200,
        "output": {
            "user_answer": False,
            "response": [
                {
                    "type": "text",
                    "content": response["response"],
                    "recommendations": response["recommendations"],
                }
            ]
        }
    }