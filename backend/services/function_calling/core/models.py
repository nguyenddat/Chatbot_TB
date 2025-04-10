import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from backend.services.function_calling.core.parser import (
    function_calling_parser,
    chat_history_response_parser,
    welcome_parser,
    procedure_parser
)

from backend.services.function_calling.core.prompts import *

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-4o", temperature=0
)


def get_chat_completion(task: str, params: dict):
    """
    Get chat completion from the LLM.
    """
    prompt, parser = get_prompt_template(task=task)

    chain = prompt | llm | parser

    response = chain.invoke(params).dict()
    print(response)
    return response


def get_prompt_template(task: str):
    if task == "function_calling":
        parser = function_calling_parser
        prompt_template = function_calling_prompt
    
    elif task == "welcome":
        parser = welcome_parser
        prompt_template = welcome_agent_prompt
    
    elif task == "procedure":
        parser = procedure_parser
        prompt_template = procedure_agent_prompt
    
    elif task == "chat_history":
        parser = chat_history_response_parser
        prompt_template = chat_history_prompt
    
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", prompt_template + """{format_instructions}"""),
            ("human", "{question}"),
        ]
    ).partial(format_instructions=parser.get_format_instructions())

    return prompt_template, parser
