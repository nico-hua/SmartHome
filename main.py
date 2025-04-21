from graph.graph import graph
import uuid
from utils.log_util import Logger

if __name__ == '__main__':
    # graph_png = graph.get_graph().draw_mermaid_png()
    # with open("smart_home.png", "wb") as f:
    #     f.write(graph_png)
    
    # 初始化状态
    initial_state = {
        "instruction": "你好",
        "user_location": "living_room",
        "instruction_history": [],
        "messages": []
    }

    thread_id = str(uuid.uuid4())
    thread = {"configurable": {"thread_id": thread_id}}

    logger = Logger()

    # 执行图
    messages = graph.invoke(initial_state, thread)

    while True:
        user_feedback = input("您还有什么指示？（输入空内容退出）: ")
        if not user_feedback:
            break

        new_thread_id = str(uuid.uuid4())
        new_thread = {"configurable": {"thread_id": new_thread_id}}

        new_initial_state = {
            "instruction": user_feedback,
            "user_location": messages["user_location"],
            "instruction_history": messages["instruction_history"] + [f"User:{messages['instruction']}"]+[f"AI:{messages['clarify_response'].instruction_response}"],
            "messages": []
        }

        messages = graph.invoke(new_initial_state, new_thread)