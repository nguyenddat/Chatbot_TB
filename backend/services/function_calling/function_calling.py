from typing import *

from backend.services.function_calling.functions import (
    thu_tuc
)
from backend.services.function_calling.core import (
    models,
    chat_history
)

function_descriptions = "\n".join([
    f"{id}: {description}" for id, description in thu_tuc.thu_tucs.items()
])
print(function_descriptions)


def function_calling(question: str, db: Any):
    response = models.get_chat_completion(
        task = "function_calling", 
        params = {
            "question": question, 
            "function_descriptions": function_descriptions,
            # "chat_history": chat_history.chat_history_mananger.to_string()
        }
    )

    if response["function_id"] == "":
        return {"response": response["response"], "recommendations": response["recommendations"]}
    
    else:
        thu_tuc_id = response["function_id"]
        thu_tuc_params = response["function_params"]
        if int(thu_tuc_id) not in thu_tuc.thu_tucs:
            raise ValueError("Thủ tục không tồn tại")
        
        thu_tuc_duoc_chon = thu_tuc.get_by_id(id = thu_tuc_id, params = thu_tuc_params)

        response = {
            "response": thu_tuc.to_string(thu_tuc_duoc_chon),
            "recommendations": response["recommendations"]
        }
        return response