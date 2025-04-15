from services.chatbot_agents.llm_clients.clients import get_chat_completion
from services.chatbot_agents.agents.agents import agent_descriptions

class AgentSelector:    
    def get_response(self, question, chat_history):
        response = get_chat_completion(
            task = "agent_selector",
            params = {
                "agent_descriptions": agent_descriptions,
                "question": question,
                "chat_history": chat_history
            }
        )

        return response

agent_selector = AgentSelector()


