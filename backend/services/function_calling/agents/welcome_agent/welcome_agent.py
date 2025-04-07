from services.function_calling.core.prompts import welcome_agent_prompt
from services.function_calling.core.models import get_chat_completion
from services.function_calling.agents.procedure_agent.helpers import thu_tuc

class WelcomeAgent:
    def __init__(self):
        self.description = "Đây là agent được chuyên dụng đối với nhiệm vụ chào hỏi, giới thiệu về tính năng chức năng của hệ thống. Nếu câu hỏi, yêu cầu của người hỏi mang tính chào hỏi, xã giao hoặc yêu cầu  chung chung không cụ thể thủ tục cần thiết thì đây là agent nên được ưu tiên."

        self.promp = welcome_agent_prompt
    

    def get_response(self, question, chat_history):
        response = get_chat_completion(
            task = "welcome",
            params = {
                "procedure_descriptions": thu_tuc.procedure_descriptions,
                "question": question,
                "chat_history": chat_history
            }
        )

        return response

welcome_agent = WelcomeAgent()


