from utils.logger import Logger
from langchain_community.embeddings import DashScopeEmbeddings
from chromadb import PersistentClient
from utils.redis_util import RedisUtils
import json

class RAGModule:
    def __init__(self, persist_directory="./chroma_db"):
        """
        初始化 RAGModule 模块
        :param persist_directory: 持久化存储目录
        """
        self.logger = Logger()
        self.embedding_model = DashScopeEmbeddings()
        # 初始化 Chroma 向量数据库并启用持久化存储
        self.chroma_client = PersistentClient(path=persist_directory)
        self.collection = self.init_chroma_collection()
        self.redis = RedisUtils()
    
    def init_chroma_collection(self):
        """
        初始化或加载 Chroma 集合
        """
        collection_name = "clarified_instructions"
        # 获取所有集合的名称
        existing_collections = self.chroma_client.list_collections()
        if collection_name in existing_collections:
            return self.chroma_client.get_collection(name=collection_name)
        else:
            return self.chroma_client.create_collection(name=collection_name)
        
    def embed_and_store_instruction(self, instruction, uuid):
        """
        将指令嵌入并存储到 Chroma 向量数据库中
        """
        embedding = self.embedding_model.embed_query(instruction)
        self.collection.add(
            ids=[uuid],
            documents=[instruction],
            embeddings=[embedding]
        )
        self.logger.log(f"RAG:指令 {instruction} 嵌入并存储到 Chroma 向量数据库中")
        return True
    
    def retrieve_similar_instructions(self, query_text, top_k=1):
        """
        根据查询文本检索相似的指令
        """
        query_embedding = self.embedding_model.embed_query(query_text)
        result = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        self.logger.log(f"RAG:根据查询文本检索相似的指令，查询文本：{query_text}，top_k：{top_k}，检索到的结果：{result}")
        return result
    
    def get_similar_instruction_info(self, instruction):
        """
        获取与当前指令相似的指令的执行结果
        """
        result = self.retrieve_similar_instructions(instruction)
        ids = result['ids'][0]
        documents = result['documents'][0]
        if ids == []:
            return None
        else:
            similar_instruction = documents[0]
            similar_instruction_uuid = ids[0]
            similar_instruction_devices = self.redis.get_value(f"Filter:{similar_instruction_uuid}")
            similar_instruction_feedback = self.redis.get_value(f"Feedback:{similar_instruction_uuid}")
            similar_instruction_plan = self.redis.get_value(f"Plan:{similar_instruction_uuid}")
            similar_instruction_info = json.dumps({
                "status": "success",
                "instruction": similar_instruction,
                "devices": similar_instruction_devices,
                "plan": similar_instruction_plan,
                "feedback": similar_instruction_feedback
            }, ensure_ascii=False)
            self.logger.log(f"RAG:{similar_instruction_info}")
            return similar_instruction_info