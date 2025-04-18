from state.globalState import GlobalState

# 用于判断是否需要调用工具
def should_continue(state: GlobalState):
    messages = state['messages']
    last_message = messages[-1]
    # 如果调用的工具 ClarifyResponse，则转到 structured_response 节点
    if len(last_message.tool_calls) == 1 and last_message.tool_calls[0]['name'] == "ClarifyResponse":
        return "structured_response"
    else:
        return "continue"