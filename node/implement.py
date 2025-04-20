from state.global_state import GlobalState
import threading
from langchain_core.messages import SystemMessage, HumanMessage
from utils.log_util import Logger
from llm.model import llm
from device.device_api_info import device_api_info
from node.generate_plan import DeviceAction
from device.device import light, curtain, air_conditioner, television, audio_player
from utils.mysql_util import MySQLUtils

implement_device_action_system_prompt = """You are a Python assistant that helps generate device control code based on structured API descriptions.
"""

implement_device_action_human_prompt = """
Device ID:
{device_id}

Device Type:
{device_type}

API Description:
{api_info}

Task:
Given the following list of natural language actions:
{actions}

Generate Python code that calls the corresponding device control APIs.  
Each function should be called using the format `{device_type}.function_name(...)`.  
Use the device ID as the required `device_id` parameter in all function calls.

For example:
If action is "Turn on the light", and the API method is `turn_on(device_id: str)`, generate:  
`light.turn_on(device_id="light_living_room")`

If action is "Set brightness level=80", and the API method is `set_brightness(device_id: str, brightness: int)`, generate:  
`light.set_brightness(device_id="light_living_room", brightness=80)`

Only return valid Python code. No extra explanation.
"""

def implement_device_action(device_action: DeviceAction):
    device_id = device_action.device_id
    actions = device_action.actions
    # 从数据库中查询获取 device_type
    mysql = MySQLUtils()
    device_type = mysql.get_device_type_by_id(device_id)
    # 获取对应类型的设备API描述
    api_info = device_api_info[device_type]
    human_message = implement_device_action_human_prompt.format(device_id=device_id,device_type=device_type,api_info=api_info,actions=actions)
    messages = [SystemMessage(content=implement_device_action_system_prompt)]+[HumanMessage(content=human_message)]
    # 尝试最多两次（初始+错误修复）
    response = llm.invoke(messages)
    # 将消息加入方便出错反馈
    messages.append(response)
    # 提取代码
    if "```python" in response.content:
            python_code = response.content.split("```python")[1].split("```")[0].strip()
    else:
            python_code = response.content.strip()
    # 执行代码
    try:
        exec(python_code)
        return
    except Exception as e:
        error_msg = str(e)
        logger = Logger()
        logger.log(f"执行出错: {error_msg}", level="ERROR")
        messages.append(HumanMessage(content=f"❌ The above code failed with the following error:\n{error_msg}\nPlease correct the code and return ONLY valid Python code."))
        # 将错误信息加入执行
        response = llm.invoke(messages)
        # 提取代码
        if "```python" in response.content:
                python_code = response.content.split("```python")[1].split("```")[0].strip()
        else:
                python_code = response.content.strip()
        try:
            exec(python_code)
            return
        except Exception as e:
            error_msg = str(e)
            print(f"[❌ FINAL FAIL] {device_id} 设备执行失败: {error_msg}")

def implement(state: GlobalState):
    plan = state.get("plan", [])
    threads = []
    # 使用多线程实现
    for device_action in plan:
        thread = threading.Thread(target=implement_device_action, args=(device_action,))
        thread.start()
        threads.append(thread)
    # 等待所有线程完成
    for thread in threads:
        thread.join()
    print("✅ All device actions completed.")
