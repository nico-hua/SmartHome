from state.globalState import GlobalState
from langgraph.graph import END

# 处理用户反馈
def human_feedback(state: GlobalState):
    user_feedback = state.get('instruction', '')
    if not user_feedback:
        return END
    else:
        return 'clarify_instruction'