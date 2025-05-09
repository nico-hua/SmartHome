from state.global_state import GlobalState, ClarifyResponse
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
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        try:
            response = ClarifyResponse(**last_message.tool_calls[0]['args'])
        except Exception as e:
            logger.log(f"structured_response 1: {e}")
            response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

    # ```json 标记格式
    elif "```json" in content:
        try:
            response = ClarifyResponse(**json.loads(content.split("```json")[1].split("```")[0].strip()))
        except Exception as e:
            logger.log(f"structured_response 2: {e}")
            response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

    # ✦FUNCTION✿: 前缀格式
    elif "require_device" in content and "instruction_response" in content:
        # 尝试从非标准内容中提取 JSON
        args_start = content.find("{")
        args_end = content.rfind("}") + 1
        args_json = content[args_start:args_end]
        try:
            response = ClarifyResponse(**json.loads(args_json))
        except Exception as e:
            logger.log(f"structured_response 3: {e}")
            response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

    else:
        logger.log("structured_response: 无法解析的输出格式")
        response = ClarifyResponse(instruction_response="发生错误，请稍后重试", require_device=False)

    return {**state, "clarify_response": response}
