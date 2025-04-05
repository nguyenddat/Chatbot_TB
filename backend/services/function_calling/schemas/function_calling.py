from typing import *

from pydantic import BaseModel, Field

class FunctionCallingResponse(BaseModel):
    """
    Function calling response schema.
    """
    function_id: str = Field(..., description="Name of the function to call")
    response: str = Field(..., description="Response from the function call")
    recommendations: List[str] = Field(..., description="List of recommended functions")