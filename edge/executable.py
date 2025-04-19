from state.global_state import GlobalState
from utils.log_util import Logger

# 根据推荐的设备是否为空，选择路由
def executable(state: GlobalState):
    """ 根据用户指令是否可执行路由 """
    clarify_response = state['clarify_response']
    logger = Logger()
    if clarify_response.require_device:
        logger.log("路由到 generate_plan")
        return "generate_plan"
    else:
        logger.log("路由到 final_output")
        return "final_output"
