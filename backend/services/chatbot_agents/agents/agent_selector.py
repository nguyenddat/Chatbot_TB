from services.chatbot_agents.llm_clients.clients import get_chat_completion
from services.chatbot_agents.agents.agents import agent_descriptions

class AgentSelector:    
    def get_response(self, question, chat_history):
        response, tokens = get_chat_completion(
            task = "agent_selector",
            params = {
                "agent_descriptions": agent_descriptions,
                "question": question,
                "chat_history": chat_history
            }
        )

        return response, tokens

agent_selector = AgentSelector()


