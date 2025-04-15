from services.chatbot_agents.agents.procedure_selector import procedure_selector
from services.chatbot_agents.agents.welcome_agent import welcome_agent


agents = {
    "procedure": procedure_selector,
    "welcome": welcome_agent
}

agent_descriptions = {
    "procedure": procedure_selector.description,
    "welcome": welcome_agent.description
}
