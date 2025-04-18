from state.globalState import GlobalState
from state.globalState import ClarifyResponse
from utils.log_util import Logger

# 结构化输出节点
def structured_response(state: GlobalState):
    """ 结构化输出 """
    response = ClarifyResponse(**state['messages'][-1].tool_calls[0]['args'])
    # 日志
    logger = Logger()
    logger.log(f"是否需要操作设备: {response.require_device} 回复：{response.instruction_response}")
    return {**state, "clarify_response": response}
