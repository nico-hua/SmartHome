from state.globalState import GlobalState
from state.globalState import ClarifyResponse

# 结构化输出节点
def structured_response(state: GlobalState):
    response = ClarifyResponse(**state['messages'][-1].tool_calls[0]['args'])
    return {**state, "clarify_response": response}
