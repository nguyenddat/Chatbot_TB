import os

import faiss
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_community.docstore.in_memory import InMemoryDocstore

from services.chatbot_agents.helpers.data_loader import data_loader
from services.chatbot_agents.llm_clients.clients import embeddings

data_path = os.path.join(os.getcwd(), "backend", "services", "chatbot_agents", "data", "vector_store")

class Retriever:
    def __init__(self):
        self.data_path = data_path
        self._post_init()

    def _post_init(self):
        if os.path.exists(self.data_path):
            self.ingest()
        
        else:
            self.build()
            
    def build(self):
        texts = data_loader.load()

        index = faiss.IndexFlatL2(1024)

        vector_store = FAISS(
            embedding_function = embeddings,
            index = index,
            docstore = InMemoryDocstore(),
            index_to_docstore_id = {}
        )

        vector_store.add_documents(texts)
        vector_store.save_local(self.data_path)
        self.retriever = VectorStoreRetriever(vectorstore=vector_store)
        return self
    
    def ingest(self):
        vector_store = FAISS.load_local(self.data_path, embeddings, allow_dangerous_deserialization=True)
        self.retriever = VectorStoreRetriever(vectorstore=vector_store)
        return self

retriever = Retriever()