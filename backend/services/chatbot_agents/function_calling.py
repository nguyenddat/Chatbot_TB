from typing import *

from backend.services.chatbot_agents.agents.agents import agents
from backend.services.chatbot_agents.agents.agent_selector import agent_selector


def function_calling(question: str, chat_history: Any, db: Any = None):
    """ User query --> Agent selector"""
    agent_selected_id, tokens = agent_selector.get_response(question, chat_history)
    agent_selected = agents[agent_selected_id["agent_id"]]

    """ User query --> Agent selected"""
    response, new_tokens = agent_selected.get_response(question, chat_history)

    print(f"Đã request {tokens + new_tokens} tokens")
    return response