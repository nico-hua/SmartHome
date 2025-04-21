from state.global_state import GlobalState
from pydantic import BaseModel, Field
from typing import List
from llm.model import llm
from langchain_core.messages import SystemMessage, HumanMessage
from utils.log_util import Logger

# 家庭房间
DEFAULT_ROOM_NAMES = ["living_room","master_bedroom","guest_bedroom","kitchen","bathroom"] 

class ExtractedLocation(BaseModel):
    locations: List[str] = Field(description="list of room location extracted from user instruction.")

extract_location_system_prompt = """
You are a smart home AI assistant specialized in location extraction. Your primary task is to accurately identify target rooms by analyzing both current instructions and historical context.

Key Focus:
1. FIRST prioritize explicit room mentions in the current instruction
2. WHEN no room is mentioned, CAREFULLY ANALYZE the instruction history to infer the most probable location
3. Pay SPECIAL ATTENTION to maintaining context across consecutive instructions

Rules:
1. Standardize all room names to match exactly with: {room_names}
2. For implicit references:
   - Track the most recently mentioned room in the history
   - Consider ongoing activity patterns (e.g., consecutive light adjustments suggest same location)
   - Verify if the current action logically extends previous commands
3. Return empty list ONLY when:
   - No room is mentioned AND
   - No relevant context exists in history AND
   - No logical inference can be made

Output Requirements:
- Only return room names included in {room_names}
- Format strictly as a JSON list: ["room_name"] or []
- DO NOT add any explanation or extra text

Examples:
- History: "打开浴室的灯" → Instruction: "调亮客厅的灯" → Response: ["living_room"]
- History: ["打开空调", "调高温度"] → Instruction: "现在关掉" → Response: []
- History: "主卧的灯太亮了" → Instruction: "调暗一点" → Response: ["master_bedroom"]
"""

extract_location_human_prompt = """
Instruction History:
{instruction_history}

Current Instruction:
{instruction}
"""

def extract_location(state: GlobalState):
    """ 提取用户指令目标位置 """
    instruction = state['instruction']
    user_location = state['user_location']
    instruction_history = state['instruction_history']
    # 创建结构化LLM
    structured_llm = llm.with_structured_output(ExtractedLocation)  
    # 准备系统消息和用户消息，这里历史指令仅选取最近的10条指令
    system_message = extract_location_system_prompt.format(room_names=DEFAULT_ROOM_NAMES)
    human_message = extract_location_human_prompt.format(instruction_history="\n".join(instruction_history[-10:]), instruction=instruction)
    # 调用模型
    response = structured_llm.invoke([SystemMessage(content=system_message)]+[HumanMessage(content=human_message)])
    target_location = response.locations if response else []
    # 确保提取的位置信息都在 DEFAULT_ROOM_NAMES 中
    target_location = [room for room in target_location if room in DEFAULT_ROOM_NAMES]
    # 判断提取的房间位置是否为空，如果为空，则加入用户位置
    if not target_location:
        target_location = [user_location]
    logger = Logger()
    logger.log(f"提取的目标房间位置：{target_location}")
    return {**state, "target_location": target_location}