from langchain_core.output_parsers import PydanticOutputParser

from services.function_calling.schemas import (
    function_calling,
    chatbot_response,
    chat_history_response,
    procedure_response,
    welcome_response
)

function_calling_parser = PydanticOutputParser(
    pydantic_object=function_calling.FunctionCallingResponse
)

chatbot_response_parser = PydanticOutputParser(
    pydantic_object=chatbot_response.FunctionCallingResponse
)

chat_history_response_parser = PydanticOutputParser(
    pydantic_object=chat_history_response.ChatHistoryResponse
)

welcome_parser = PydanticOutputParser(
    pydantic_object=welcome_response.WelcomeAgentResponse
)

procedure_parser = PydanticOutputParser(
    pydantic_object=procedure_response.ProcedureAgentResponse
)