from fastapi import APIRouter, Depends

from backend.database.base import get_db
from backend.schemas import chatbot
from backend.services.function_calling import function_calling
from backend.services.function_calling.helpers import chat_history

router = APIRouter()


@router.post("/chatbot")
def chat_chatbot(data: chatbot.ChatChatbotRequest, db=Depends(get_db)):
    question = data.question
    chat_history_request = data.chat_history
    chat_history_format = chat_history.chat_history_mananger._format_chat_history(
        chat_history_request
    )

    agent = function_calling.function_calling(
        question=question, 
        chat_history = chat_history_format,
    )

    response = agent.get_response(question=question, chat_history=chat_history_format)

    chat_history.chat_history_mananger.add_chat_format(
        chat_history_format=chat_history_format
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
