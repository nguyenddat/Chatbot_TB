from typing import *

from backend.services.chatbot_agents.agents.welcome_agent import welcome_agent
from backend.services.chatbot_agents.agents.procedure_selector import procedure_selector
from backend.services.chatbot_agents.agents.agent_selector import agent_selector


def function_calling(question: str, chat_history: Any, db: Any = None):
    """User query --> Agent selector"""
    agent_selector_response, tokens = agent_selector.get_response(
        question, chat_history
    )
    procedure = agent_selector_response["procedure"]
    procedure_params = agent_selector_response["procedure_params"]
    print("agent_selector_response", agent_selector_response)

    print(procedure)
    if len(procedure) == 0:
        response, new_tokens = welcome_agent.get_response(question=question)

    else:
        response, new_tokens = procedure_selector.get_response(
            procedure=procedure, procedure_params=procedure_params
        )

    print(f"Đã request {tokens + new_tokens} tokens")
    return response
