from langgraph.prebuilt import ToolNode
from tool.tavily_search import tavily_search
from tool.get_room_info import get_room_info
from state.global_state import ClarifyResponse

# 定义工具列表
tools = [tavily_search, get_room_info, ClarifyResponse]

# 创建工具节点
tool_node = ToolNode(tools=tools)