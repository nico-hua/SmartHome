from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing import List, Dict

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
    instruction_history: List[str]  # 用户指令历史
    target_location: List[str]  # 目标房间位置
    environment_info: List[Dict]  # 房间描述信息
    recommended_devices: List[str]  # 推荐的物理设备类型列表
    plan: List[Dict[str, List[str]]]  # 执行计划
    plan_description: str  # 执行计划描述