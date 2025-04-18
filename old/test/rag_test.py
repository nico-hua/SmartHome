from tools.rag import RAGModule
import json

if __name__ == "__main__":
    rag = RAGModule()
    # rag.embed_and_store_instruction("狗是忠诚和友好的伴侣。", "uuid1")
    # rag.embed_and_store_instruction("猫是一种独立的宠物，通常喜欢自己的空间。", "uuid2")
    # rag.embed_and_store_instruction("金鱼是新手的理想宠物，照顾起来相对简单。", "uuid3")
    # rag.embed_and_store_instruction("鹦鹉是聪明的鸟类，能够模仿人类的语言。", "uuid4")
    # rag.embed_and_store_instruction("兔子是一种社交性很强的动物，喜欢有足够的空间活动。", "uuid5")
    # rag.embed_and_store_instruction("老虎是一种凶猛的动物。", "uuid6")
    result = rag.retrieve_similar_instructions("打开卧室的灯", 1)
    if 'ids' in result and result['ids']:
        ids = result['ids'][0]  # 获取 ids 列表中的第一个元素
        documents = result['documents'][0] if 'documents' in result else []

        if ids:  # 确保 ids 不为空
            for i, doc in zip(ids, documents):
                print(f"ID: {i}")
                print(f"Document: {doc}")
        else:
            print("没有找到匹配的 ID。")
    else:
        print("检索结果中没有 ids 字段或 ids 为空。")