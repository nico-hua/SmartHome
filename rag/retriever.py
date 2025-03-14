from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from utils.logger import Logger

class Retriever:
    def __init__(self):
        self.logger = Logger()
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = FAISS.load_local("vector_store", self.embeddings)

    def retrieve(self, query, threshold=0.7):
        try:
            docs = self.vector_store.similarity_search_with_score(query)
            filtered_docs = [doc for doc, score in docs if score >= threshold]
            self.logger.log(f"Retrieved Documents: {filtered_docs}")
            return filtered_docs
        except Exception as e:
            self.logger.log(f"Retrieval Error: {str(e)}", level="ERROR")
            return []