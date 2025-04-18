from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from state.globalState import GlobalState
from node.tool_node import tool_node
from node.structured_response import structured_response
from node.clarify_instruction import clarify_instruction
from edge.should_continue import should_continue

builder = StateGraph(GlobalState)

# 添加节点
builder.add_node("clarify_instruction", clarify_instruction)
builder.add_node("tools", tool_node)
builder.add_node("structured_response", structured_response)

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
builder.add_edge("structured_response", END)

# 添加 memory
memory = MemorySaver()

graph = builder.compile(checkpointer=memory)