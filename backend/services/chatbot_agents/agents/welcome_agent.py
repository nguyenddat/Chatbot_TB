from backend.services.chatbot_agents.llm_clients.prompts import welcome_agent
from backend.services.chatbot_agents.llm_clients.clients import get_chat_completion
from backend.services.chatbot_agents.helpers.procedures import get_random_thu_tuc

class WelcomeAgent:
    def __init__(self):
        self.description = "Đây là agent được chuyên dụng đối với nhiệm vụ chào hỏi, giới thiệu về tính năng chức năng của hệ thống và tư vấn tủ tục phù hợp với người dùng. Nếu câu hỏi, yêu cầu của người hỏi mang tính chào hỏi, xã giao thì đây là agent nên được ưu tiên. Hơn nữa, nếu người dùng hỏi về thủ tục nào phù hợp với bản thân hoặc đại khái là mang tính chất tư vấn và giới thiệu, agent này nên được ưu tiên. Nếu người dùng hỏi về đặc biệt 1 thủ tục cụ thể, không nên sử dụng agent này."

        self.promp = welcome_agent.welcome_agent_prompt
    

    def get_response(self, question, chat_history):
        response, tokens = get_chat_completion(
            task = "welcome",
            params = {
                "procedure_descriptions": get_random_thu_tuc(),
                "question": question,
                "chat_history": chat_history
            }
        )

        return response, tokens

welcome_agent = WelcomeAgent()


