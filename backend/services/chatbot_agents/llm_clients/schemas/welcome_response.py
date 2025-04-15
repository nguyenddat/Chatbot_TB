from typing import *

from pydantic import BaseModel, Field

class WelcomeAgentResponse(BaseModel):
    """
    Function calling response schema.
    """
    response: str = Field(..., description="Phản hồi")
    recommendations: List[str] = Field(..., description="Gợi ý câu hỏi")
