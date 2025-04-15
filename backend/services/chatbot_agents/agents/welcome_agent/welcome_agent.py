from backend.services.chatbot_agents.core.prompts import welcome_agent_prompt
from backend.services.chatbot_agents.core.models import get_chat_completion
from backend.services.chatbot_agents.agents.procedure_agent.helpers import thu_tuc

class WelcomeAgent:
    def __init__(self):
        self.description = "Đây là agent được chuyên dụng đối với nhiệm vụ chào hỏi, giới thiệu về tính năng chức năng của hệ thống và tư vấn tủ tục phù hợp với người dùng. Nếu câu hỏi, yêu cầu của người hỏi mang tính chào hỏi, xã giao thì đây là agent nên được ưu tiên. Hơn nữa, nếu người dùng hỏi về thủ tục nào phù hợp với bản thân hoặc đại khái là mang tính chất tư vấn và giới thiệu, agent này nên được ưu tiên. Nếu người dùng hỏi về đặc biệt 1 thủ tục cụ thể, không nên sử dụng agent này."

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


