from services.function_calling.core.prompts import procedure_agent_prompt
from services.function_calling.core.models import get_chat_completion
from services.function_calling.agents.procedure_agent.helpers import thu_tuc

class ProcedureAgent:
    def __init__(self):
        self.description = "Đây là agent được chuyên dụng đối với nhiệm vụ hỏi đáp về một thủ tục cụ thể. Nếu người dùng cần hỏi về một thủ tục nào đó cụ thể, agent nên được ưu tiên"

        self.propmt = procedure_agent_prompt

    
    def get_response(self, question, chat_history):
        response = get_chat_completion(
            task = "procedure",
            params = {
                "function_descriptions": thu_tuc.procedure_descriptions,
                "question": question,
                "chat_history": chat_history
            }
        )

        if response["function_id"] == "":
            return {"response": response["response"], "recommendations": response["recommendations"]}
        
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

procedure_agent = ProcedureAgent()
        

