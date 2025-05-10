from state.global_state import GlobalState, ClarifyResponse
from pydantic import BaseModel, Field
from typing import List
from utils.convert_util import convert_environment_info
from utils.log_util import Logger
from llm.model import llm
from langchain_core.messages import SystemMessage, HumanMessage
import json

class RecommendedDevice(BaseModel):
    recommended_devices: List[str] = Field(description="list of device types inferred from the user's instruction and the available devices in the environment.")

# 家庭房间
DEFAULT_DEVICE_TYPES = ["light","audio_player","curtain","television","air_conditioner", "ventilation_fan", "humidifier", "air_purifier", "range_hood", "heater", "window"] 

recommend_device_system_prompt = """You are a smart home AI assistant. Your task is to infer what types of smart devices in the room are needed to fulfill the user's instruction.

You are provided with:
1. The list of available devices in the room, including their device_id, device_type, location, description and status.

You MUST follow these rules:
1. Only recommend device types that actually exist in the room where the action is to happen.
2. If the instruction does not specify a room, assume it refers to the user's current room. User's current location: {user_location}.
3. If a device type is relevant to the instruction but not present in the room (Room Device and Status Information), DO NOT recommend it.
4. Consider scenario-based intentions (e.g., 'I want to have a party' → may need related device) only if those devices are available in the room.
5. Only return a JSON list of device types, such as ["light", "air_conditioner"] or [].
6. If all devices in the room are unavailable or unsupported for the given instruction, return an empty list `[]`.
7. Do NOT add any explanation or extra text.
8. If the user's instruction intention is unclear, you may need to infer it based on the user's instruction history.

Room Device and Status Information (Format: [Room] - [Device ID] - [Device Type]- [Loaction]- [Description] - [Status]):
{environment_info}

Examples:
- Instruction: "打开客厅的灯和音响" (living_room has light and audio_player) → ["light", "audio_player"]
- Instruction: "我想听歌" (User's current location is master_bedroom, but master_bedroom does not have audio_player) → []
"""

recommend_device_human_prompt = """
Recent Instruction History:
{instruction_history}

Instruction:
{instruction}
"""

def filter_device(state: GlobalState):
    """ 根据用户指令推荐可能用到的物理设备 """
    instruction = state['instruction']  
    user_location = state['user_location']
    environment_info = state['environment_info'] 
    instruction_history = state['instruction_history']
    # environment_info 转换为 llm 易于理解的格式
    environment_info = convert_environment_info(environment_info)
    # 创建结构化LLM
    structured_llm = llm.with_structured_output(RecommendedDevice)  
    # 准备系统消息
    system_message = recommend_device_system_prompt.format(environment_info=environment_info, user_location=user_location)
    human_message = recommend_device_human_prompt.format(instruction_history="\n".join(instruction_history[-10:]), instruction=instruction)
    # 调用模型
    response = structured_llm.invoke([SystemMessage(content=system_message)]+[HumanMessage(content=human_message)])
    recommended_devices = []
    if response:
        if isinstance(response, RecommendedDevice):
            recommended_devices = response.recommended_devices
        else:
            try:
                recommended_devices = json.loads(response.content)
            except json.JSONDecodeError:
                recommended_devices = []
    # 确保推荐的设备类型都在 DEFAULT_DEVICE_TYPES 中
    recommended_devices = [device for device in recommended_devices if device in DEFAULT_DEVICE_TYPES]
    logger = Logger()
    logger.log(f"推荐的物理设备：{recommended_devices}")
    clarify_response = ClarifyResponse(instruction_response="", require_device=True)
    # 判断提取的设备类型是否为空，
    if not recommended_devices:
        clarify_response.require_device = False
        clarify_response.instruction_response = "缺乏支持的设备类型或者设备功能不支持"
        return {**state, "recommended_devices": [], "clarify_response": clarify_response}
    # 如果不为空，则过滤环境信息
    filtered_environment_info = []
    for room_data in state['environment_info']:
        for room_name, devices in room_data.items():
            filtered_devices = []
            for device in devices:
                if device.device_info.device_type in recommended_devices:
                    filtered_devices.append(device)
            filtered_environment_info.append({room_name: filtered_devices})
    return {**state, "environment_info":filtered_environment_info, "recommended_devices": recommended_devices, "clarify_response": clarify_response}