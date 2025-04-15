from typing import *

from pydantic import BaseModel, Field

class ProcedureAgentResponse(BaseModel):
    function_id: str = Field(..., description="Thủ tục được chọn")
    function_params: List[str] = Field(..., description="Thông tin chi tiết của thủ tục")
    response: str = Field(..., description="Phản hồi")
    recommendations: List[str] = Field(..., description="Gợi ý câu hỏi")
