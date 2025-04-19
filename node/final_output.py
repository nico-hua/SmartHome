from state.global_state import GlobalState

def final_output(state: GlobalState):
    """ 打印用户指令回复 """
    clarify_response = state['clarify_response']
    if clarify_response.instruction_response:
        print(clarify_response.instruction_response)
    return state