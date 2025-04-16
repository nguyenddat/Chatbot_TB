from fastapi import APIRouter, Depends

from backend.database.base import get_db
from backend.schemas import chatbot
from backend.services.chatbot_agents import function_calling
from backend.services.chatbot_agents.helpers import chat_history

router = APIRouter()


@router.post("/chatbot")
def chat_chatbot(data: chatbot.ChatChatbotRequest, db=Depends(get_db)):
    question = data.question
    chat_history_request = data.chat_history

    crop = min(6, len(chat_history_request))
    chat_history_request = chat_history_request[-crop:]

    chat_history_format = chat_history.chat_history_mananger._format_chat_history(
        chat_history_request
    )

    response = function_calling.function_calling(
        question=question, chat_history=chat_history_format, db=db
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
            ],
        },
    }
