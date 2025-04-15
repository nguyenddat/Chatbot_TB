from typing import *

from pydantic import BaseModel, Field

class ProcedureAgentResponse(BaseModel):
    procedure_id: str = Field(..., description="Thủ tục được chọn")
    response: str = Field(..., description="Phản hồi")
    recommendations: List[str] = Field(..., description="Gợi ý câu hỏi")
