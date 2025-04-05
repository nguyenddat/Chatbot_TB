from langchain_core.output_parsers import PydanticOutputParser

from services.function_calling.schemas import (
    function_calling,
    chatbot_response
)

function_calling_parser = PydanticOutputParser(
    pydantic_object=function_calling.FunctionCallingResponse
)

chatbot_response_parser = PydanticOutputParser(
    pydantic_object=chatbot_response.FunctionCallingResponse
)