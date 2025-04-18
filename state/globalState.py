from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing import List

# clarify_instruction 标准输出
class ClarifyResponse(BaseModel):
    """ clarify and reply output """
    require_device: bool = Field(description="whether need to operate home physical equipment")
    instruction_response: str = Field(decription="user instruction response")

# 全局 state
class GlobalState(MessagesState):
    instruction: str  # 用户指令
    user_location: str  # 用户所在房间位置
    clarify_response: ClarifyResponse  # 用户指令回复
    user_feedback: str  # 用户反馈
    instruction_history: List[str]  # 用户指令历史