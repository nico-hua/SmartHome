from utils.log_util import Logger
from chromadb import PersistentClient
from langchain_community.embeddings import DashScopeEmbeddings
from utils.log_util import Logger
import json

class ChromaUtils:
    def __init__(self, persist_directory="./chroma_db"):
        """
        初始化 ChromaUtils 类
        :param persist_directory: 持久化存储目录
        """
        self.logger = Logger()
        self.embedding_model = DashScopeEmbeddings()
        # 初始化 Chroma 向量数据库并启用持久化存储
        self.chroma_client = PersistentClient(path=persist_directory)
        self.collection = self.init_chroma_collection()

    def init_chroma_collection(self):
        """
        初始化 Chroma 向量数据库
        :return: Chroma 向量数据库
        """
        collection_name = "device_api"
        # 获取所有集合的名称
        existing_collections = self.chroma_client.list_collections()
        if collection_name in existing_collections:
            # self.logger.log(f"集合 {collection_name} 已存在")
            return self.chroma_client.get_collection(name=collection_name)
        else:
            # self.logger.log(f"创建新的集合: {collection_name}")
            return self.chroma_client.create_collection(name=collection_name)
        
    def embed_and_store_instruction(self, id, description, api, args_num):
        """
        将指令嵌入并存储到 Chroma 向量数据库中
        """
        api_json = {
            "id": id,
            "description": description,
            "api": api,
            "args_num": args_num
        }
        api_data = json.dumps(api_json, ensure_ascii=False)
        embedding = self.embedding_model.embed_query(description)
        # 添加到向量数据库
        self.collection.add(
            ids=[id],
            documents=[api_data],
            embeddings=[embedding]
        )
        self.logger.log(f"指令 {id} 嵌入并存储成功")

    def retrieve_similar_instructions(self, query_text, top_k=1):
        """
        根据查询文本检索相似的指令
        """
        query_embedding = self.embedding_model.embed_query(query_text)
        result = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        # self.logger.log(f"根据查询文本检索相似的api，查询文本：{query_text}，top_k：{top_k}，检索到的api：{result}")
        return result["documents"][0][0]

    
