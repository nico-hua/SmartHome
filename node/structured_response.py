from state.globalState import GlobalState
from state.globalState import ClarifyResponse
from utils.log_util import Logger
import json

# 结构化输出节点
def structured_response(state: GlobalState):
    """处理结构化输出，兼容多种格式：
    1. 标准 tool_calls 格式
    2. ```json 标记格式
    3. ✦FUNCTION✿: 前缀格式
    """
    logger = Logger()
    last_message = state["messages"][-1]
    content = last_message.content
    response = None

    # 标准 tool_calls 格式
    if hasattr(last_message, "tool_calls"):
        try:
            response = ClarifyResponse(**last_message.tool_calls[0]['args'])
        except Exception as e:
            logger.log(f"structured_response: {e}")
            response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

    # ```json 标记格式
    if "```json" in content:
        try:
            response = ClarifyResponse(**json.loads(content.split("```json")[1].split("```")[0].strip()))
        except Exception as e:
            logger.log(f"structured_response: {e}")
            response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

    # ✦FUNCTION✿: 前缀格式
    if "require_device" in content and "instruction_response" in content:
        # 尝试从非标准内容中提取 JSON
        args_start = content.find("{")
        args_end = content.rfind("}") + 1
        args_json = content[args_start:args_end]
        try:
            response = ClarifyResponse(**json.loads(args_json))
        except Exception as e:
            logger.log(f"structured_response: {e}")
            response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

    return {**state, "clarify_response": response}
