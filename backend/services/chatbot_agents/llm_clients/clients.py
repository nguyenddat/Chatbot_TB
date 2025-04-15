import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate

from services.chatbot_agents.llm_clients.parsers import (
    function_calling_parser,
    chat_history_response_parser,
    welcome_parser,
    procedure_parser
)

from services.chatbot_agents.llm_clients.prompts import (
    agent_selector,
    chat_history,
    procedure_selector,
    welcome_agent
)

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions = 1024
)


def get_chat_completion(task: str, params: dict):
    """
    Get chat completion from the LLM.
    """
    prompt, parser = get_prompt_template(task=task)

    chain = prompt | llm | parser

    response = chain.invoke(params).dict()
    return response


def get_prompt_template(task: str):
    if task == "agent_selector":
        parser = function_calling_parser
        prompt_template = agent_selector.agent_selector_prompt
    
    elif task == "welcome":
        parser = welcome_parser
        prompt_template = welcome_agent.welcome_agent_prompt
    
    elif task == "procedure":
        parser = procedure_parser
        prompt_template = procedure_selector.procedure_selector_prompt
    
    elif task == "chat_history":
        parser = chat_history_response_parser
        prompt_template = chat_history.chat_history_prompt
    
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", prompt_template + """{format_instructions}"""),
            ("human", "{question}"),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    return prompt_template, parser
