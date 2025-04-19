from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from state.global_state import GlobalState
from node.tool_node import tool_node
from node.structured_response import structured_response
from node.clarify_instruction import clarify_instruction
from node.final_output import final_output
from node.extract_location import extract_location
from node.get_environment_info import get_environment_info
from node.recommend_device import recommend_device
from node.generate_plan import generate_plan
from node.implement import implement
from node.human_feedback import human_feedback
from edge.should_continue import should_continue
from edge.query_or_control import query_or_control
from edge.executable import executable

builder = StateGraph(GlobalState)

# 添加节点
builder.add_node("clarify_instruction", clarify_instruction)
builder.add_node("tools", tool_node)
builder.add_node("structured_response", structured_response)
builder.add_node("final_output", final_output)
builder.add_node("extract_location", extract_location)
builder.add_node("get_environment_info", get_environment_info)
builder.add_node("recommend_device", recommend_device)
builder.add_node("generate_plan", generate_plan)
builder.add_node("implement", implement)
builder.add_node("human_feedback", human_feedback)

# 添加边
builder.add_edge(START, "clarify_instruction")
builder.add_conditional_edges(
    "clarify_instruction",
    should_continue,
    {
        "continue": "tools",
        "structured_response": "structured_response",
    }
)
builder.add_edge("tools", "clarify_instruction")
builder.add_conditional_edges(
    "structured_response",
    query_or_control,
    {
        "final_output": "final_output",
        "extract_location": "extract_location",
    }
)
builder.add_edge("extract_location", "get_environment_info")
builder.add_edge("get_environment_info", "recommend_device")
builder.add_conditional_edges(
    "recommend_device",
    executable,
    {
        "generate_plan": "generate_plan",
        "final_output": "final_output",
    }
)
builder.add_edge("generate_plan", "implement")
builder.add_edge("generate_plan", "final_output")
builder.add_edge("final_output", "human_feedback")
builder.add_conditional_edges(
    "human_feedback",
    human_feedback,
    ["clarify_instruction", END]
)

# 添加 memory
memory = MemorySaver()

graph = builder.compile(interrupt_before=['human_feedback'], checkpointer=memory)