from datetime import datetime
from langchain_core.messages import SystemMessage, HumanMessage
from state.globalState import GlobalState
from llm.model import llm
from node.tool_node import tools

clarify_instruction_system_prompt = """
你是一个贴心的智能家居AI助手，任务是判断用户指令是否需要操作设备，并用自然、口语化的中文回复。

一下信息可供参考：
1. 当前用户位置：{user_location}
2. 当前时间：{current_time}
3. 设备状态信息(格式: [Room] - [Device ID] - [Device Type]- [Loaction]- [Description] - [Device Status])：你可以通过调用 get_room_info 工具获取
4. 用户当前指令
5. 用户历史指令（用于上下文推断）

必须遵守以下规则：

【判断规则】
1. ✅ 需要设备操作（require_device = true）：
   - 控制设备开关或调节参数（如亮度、音量、温度等），且设备状态不符合指令（如"开灯"且灯是关的）
   - 场景意图且环境支持的用户指令（如"开派对"且存在可操控的灯光音响等设备）

2. ❌ 不需要设备操作（require_device = false）：
   - 查询家庭设备状态（如"灯开着吗？"）
   - 日常对话（如"你好"、"谢谢"）
   - 指令要求设备开关或调节，设备已满足目标状态（如"开灯"且灯是开的）

【位置推断规则】
1. 优先使用用户当前指令明确指定的位置
2. 若无明确指定，你需要结合用户历史指令进行推断
3. 若仍无法确定，默认使用用户当前位置{user_location}

【操作规则】
- 用户指令与设备有关时，如查询设备或者可能需要操作设备，都必须先调用 get_room_info 工具获取设备状态信息，然后进行回复
- 如果用户指令是“打开 / 关闭 / 设置设备”，但当前设备状态已经满足这个指令（如灯已经开、音量已经是目标值），则不需要操作设备（require_device = false），回复设备状态即可
- 需要操作设备时，require_device为true，instruction_response保持为空：""
- 不理解用户指令时，你需要结合历史指令推断，必要时提问（require_device = false）
- 你可以使用 tavily_search_results_json 工具进行网络搜索获取高实时性信息
- 如果你已经知道如何回复用户指令或者通过调用工具获取相关信息后总结出了答案，立即调用 ClarifyResponse 工具以结构化输出
- 你最后必须使用 ClarifyResponse 工具以结构化输出
"""

clarify_instruction_human_prompt = """ 
Instruction History: {instruction_history}

Current Instruction: {instruction} """

def clarify_instruction(state: GlobalState): 
    """  判断用户指令是否需要操作设备，并生成回复 """
    instruction = state['instruction'] 
    user_location = state['user_location'] 
    instruction_history = state['instruction_history']
    # 为 llm 绑定工具并结构化输出
    model_with_tool = llm.bind_tools(tools=tools, tool_choice="auto")
    # 构造系统消息
    system_message = clarify_instruction_system_prompt.format(
        user_location=user_location,
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M")
    )
    human_message = clarify_instruction_human_prompt.format(
        instruction_history=instruction_history[-5:],  # 只取最近5条历史指令
        instruction=instruction
    )
    # 如果 state['messages'] 为空，则使用默认的消息；否则使用 state['messages']
    if not state['messages']:  # 如果 state['messages'] 为空
        messages = [SystemMessage(content=system_message), HumanMessage(content=human_message)]
    else:
        messages = [SystemMessage(content=system_message), HumanMessage(content=human_message)] + state['messages']
    response = model_with_tool.invoke(messages)
    return {"messages": [response]}