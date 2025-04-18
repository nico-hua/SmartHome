from langchain_community.chat_models import ChatTongyi

# 使用 qwen-plus 模型
llm = ChatTongyi(model="qwen-plus", temperature=0)