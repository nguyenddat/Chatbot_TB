from typing import *

from services.chatbot_agents.agents.agents import agents, agent_descriptions
from services.chatbot_agents.agents.agent_selector import agent_selector


def function_calling(question: str, chat_history: Any, db: Any = None):
    """ User query --> Agent selector"""
    agent_selected_id = agent_selector.get_response(question, chat_history)["agent_id"]
    agent_selected = agents[agent_selected_id]

    """ User query --> Agent selected"""
    response = agent_selected.get_response(question, chat_history)
    return response