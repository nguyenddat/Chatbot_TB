from backend.services.chatbot_agents.agents.procedure_agent import procedure_agent
from backend.services.chatbot_agents.agents.welcome_agent import welcome_agent


agents = {
    "procedure": procedure_agent.procedure_agent,
    "welcome": welcome_agent.welcome_agent
}

agent_descriptions = {
    "procedure": procedure_agent.procedure_agent.description,
    "welcome": welcome_agent.welcome_agent.description
}
