from services.chatbot_agents.llm_clients.prompts import welcome_agent
from services.chatbot_agents.llm_clients.clients import get_chat_completion
from services.chatbot_agents.helpers.procedures import get_random_thu_tuc

class WelcomeAgent:
    def __init__(self):
        self.promp = welcome_agent.welcome_agent_prompt
    

    def get_response(self, question):
        response, tokens = get_chat_completion(
            task = "welcome",
            params = {
                "procedure_descriptions": get_random_thu_tuc(),
                "question": question,
            }
        )

        return response, tokens

welcome_agent = WelcomeAgent()


