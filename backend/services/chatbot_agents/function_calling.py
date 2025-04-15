from typing import *

from backend.services.chatbot_agents.agents.agent import agents, agent_descriptions
from backend.services.chatbot_agents.core.models import get_chat_completion

def function_calling(question: str, chat_history: Any, db: Any = None):
    response = get_chat_completion(
        task = "function_calling", 
        params = {
            "question": question,
            "agent_descriptions": agent_descriptions,
            "chat_history": chat_history
        }
    )

    agent_id = response["agent_id"]
    if agent_id not in agents.keys():
        raise ValueError("Agent không tồn tại")
    
    agent = agents[agent_id]
    return agent