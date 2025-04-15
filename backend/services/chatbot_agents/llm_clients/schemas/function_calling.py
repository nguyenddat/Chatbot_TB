from typing import *

from pydantic import BaseModel, Field

class FunctionCallingResponse(BaseModel):
    """
    Function calling response schema.
    """
    agent_id: str = Field(..., description="Tên agent được chọn")