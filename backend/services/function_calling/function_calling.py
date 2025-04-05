from typing import *

from services.function_calling.functions import (
    thu_tuc
)
from services.function_calling.core.models import (
    get_chat_completion
)

function_descriptions = "\n".join([
    f"{id}: {description}" for id, description in thu_tuc.thu_tucs.items()
])
print(function_descriptions)


def function_calling(question: str, db: Any):
    response = get_chat_completion(task = "function_calling", params = {"question": question, "function_descriptions": function_descriptions})

    if response["function_id"] == "":
        return {"response": response["response"], "recommendations": response["recommendations"]}
    
    else:
        thu_tuc_id = response["function_id"]
        if int(thu_tuc_id) not in thu_tuc.thu_tucs:
            raise ValueError("Thủ tục không tồn tại")
        
        thu_tuc_duoc_chon = thu_tuc.get_by_id(id = thu_tuc_id)
        if not thu_tuc_duoc_chon:
            raise ValueError("Thủ tục không tồn tại")
        
        response = get_chat_completion(task = "chatbot_response", params = {
            "question": question,
            "context": thu_tuc.to_string(thu_tuc_duoc_chon)
        })
        return response