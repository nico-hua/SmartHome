from state.global_state import GlobalState
from utils.log_util import Logger
# 根据是否需要调用物理设备，路由到不同节点
def query_or_control(state: GlobalState):
    logger = Logger()
    clarify_response = state['clarify_response']
    if clarify_response.require_device:
        logger.log("路由到 extract_location")
        return "extract_location"
    else:
        logger.log("路由到 final_output")
        return "final_output"