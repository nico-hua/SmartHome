from state.globalState import GlobalState
from pydantic import BaseModel, Field
from typing import List, Dict
from langchain_core.messages import SystemMessage, HumanMessage
from utils.convert_util import convert_environment_info, convert_recommended_devices_functions
from utils.log_util import Logger
from utils.mysql_util import MySQLUtils
from llm.model import llm

class DeviceAction(BaseModel):
    device_id: str = Field(description="The device_id of the device to be controlled")
    actions: List[str] = Field(description="The actions to be performed on the device")

class ExecutionPlan(BaseModel):
    plan: List[DeviceAction] = Field(description="The list of actions to be executed")
    plan_description: str = Field(description="A description of the plan to be executed")

generate_plan_system_prompt = """You are a smart home AI assistant. Your task is to generate an executable plan to fulfill the user's instruction.

You are provided with:
1. The list of available devices in the room, including their device_id, device_type, location, description and status.
2. The functions supported by each device type (e.g., on/off, open/close, temperature control, etc.).

You MUST follow these rules:
1. Only include devices that actually exist in the room where the action is to happen. 
2. If the instruction does not specify a room, assume it refers to the user's current room. User's current location: {user_location}.
3. The plan should be expressed as a list of dictionaries with this format: 
  [{{"device_id (from the Room Device and Status Information)": ["action1", "action2"]}}, ...]
4. The actions should be derived from the supported functions of the device, and should account for the current device status. If a device already satisfies the user's request (e.g., "Turn off the light" when the light is already off), do not include it in the plan.
5. If the instruction is vague or ambiguous, infer the most likely user intention based on:
   - The current device status (e.g., if the air conditioner is already on and set to the desired temperature, no action is needed).
   - Supported functions of each device.
6. If no actionable plan can be made (e.g., devices are unavailable or unsupported for the given instruction), return an empty list.
7. If the device is already in the off status, its other status attributes indicate the settings after it is turned on.
8. Pay attention to status like power on/off, temperature, position (e.g., curtain), brightness, etc.
9. The plan should reflect only the necessary changes based on current device states.
10. Also return a brief and natural **Chinese language** description (`plan_description`) of what this plan is doing, suitable to be read aloud to the user.
11. Do not return any extra explanation or formatting. Only return structured JSON data matching the following schema:
{{
  "plan": [{{"device_id (from the Room Device and Status Information)": ["action1", "action2"]}}, ...], 
  "plan_description": "中文描述"
}}

Device Functions Description:
{devices_functions}

Room Device and Status Information (Format: [Room] - [Device ID] - [Device Type]- [Loaction]- [Description] - [Status]):
{environment_info}

Examples:
- Instruction: "打开客厅的灯和空调" → 
{{
  "plan": [
    {{"light_living_room": ["Turn on the light"]}},
    {{"ac_living_room": ["Turn on the air conditioner"]}}
  ],
  "plan_description": "正在为您打开客厅的灯和空调。"
}}

- Instruction: "关一下空调"（空调已关闭） → 
{{
  "plan": [],
  "plan_description": "空调已经关闭，无需操作。"
}}
"""

generate_plan_human_prompt = """
Recent Instruction History:
{instruction_history}

Instruction:
{instruction}
"""

def generate_plan(state: GlobalState):
    instruction = state['instruction']  
    user_location = state['user_location']
    environment_info = state['environment_info'] 
    instruction_history = state['instruction_history']
    clarify_response = state['clarify_response']
    # environment_info 转换为 llm 易于理解的格式
    environment_info = convert_environment_info(environment_info)
    recommended_devices = state['recommended_devices']
    # 获取推荐设备的功能描述
    mysql = MySQLUtils()
    recommended_devices_functions = mysql.get_recommended_devices_functions(recommended_devices)
    # recommended_devices_functions 转换为 llm 易于理解的格式
    recommended_devices_functions = convert_recommended_devices_functions(recommended_devices_functions)
    # 结构化llm
    structured_llm = llm.with_structured_output(ExecutionPlan)
    # 系统提示词
    system_message = generate_plan_system_prompt.format(
        user_location=user_location,
        environment_info=environment_info,
        devices_functions=recommended_devices_functions
    )
    human_message = generate_plan_human_prompt.format(instruction_history=instruction_history[-5:], instruction=instruction)
    response = structured_llm.invoke([
        SystemMessage(content=system_message),
        HumanMessage(content=human_message)
    ])
    plan = response.plan if response else []
    plan_description = response.plan_description if response else ""
    logger = Logger()
    logger.log(f"生成的执行计划：{plan}")
    logger.log(f"执行计划中文描述：{plan_description}")
    clarify_response.instruction_response = plan_description
    return {**state, "plan": plan, "clarify_response": clarify_response}