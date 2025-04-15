from typing import *

from pydantic import BaseModel, Field

class FunctionCallingResponse(BaseModel):
    """
    Function calling response schema.
    """
    response: str = Field(..., description="Response from chatbot")
    recommendations: List[str] = Field(..., description="Recommendations from chatbot")