from graph.graph import graph
import uuid
from log.logger import Logger

if __name__ == '__main__':
    # graph_png = graph.get_graph().draw_mermaid_png()
    # with open("smart_home.png", "wb") as f:
    #     f.write(graph_png)
    # 初始化状态
    initial_state = {
        "instruction": "你好",
        "user_location": "master_bedroom",
        "user_feedback": "",
        "instruction_history": ["打开客厅的电视"]
    }

    uuid = str(uuid.uuid4())
    thread = {"configurable":{"thread_id":uuid}}

    logger = Logger()

    # 执行图
    messages = graph.invoke(initial_state, thread)['clarify_response']
    logger.log(f"状态：{messages}")