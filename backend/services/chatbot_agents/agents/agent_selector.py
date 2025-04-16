from backend.services.chatbot_agents.llm_clients.clients import get_chat_completion

class AgentSelector:    
    def get_response(self, question, chat_history):
        response, tokens = get_chat_completion(
            task = "agent_selector",
            params = {
                "question": question,
                "chat_history": chat_history
            }
        )

        return response, tokens

agent_selector = AgentSelector()


