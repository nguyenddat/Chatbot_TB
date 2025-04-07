from typing import *

from services.function_calling.agents.agent import agents, agent_descriptions
from services.function_calling.core.models import get_chat_completion
from services.function_calling.helpers.chat_history import chat_history_mananger

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