import os

from tqdm import tqdm
from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from services.chatbot_agents.helpers.procedures import procedures

data_path = os.path.join(os.getcwd(), "backend", "services", "chatbot_agents", "data", "procedures")

class DataLoader:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )

        self.data_path = data_path
        self._post_init()

    def _post_init(self):
        if os.path.exists(data_path):
            return
        
        else:
            os.makedirs(data_path)
            for procedure, description in procedures.items():
                with open(
                    os.path.join(self.data_path, f'{procedure}.txt'), "w", encoding = "utf-8"
                ) as file:
                    file.write(description)

    def load(self):
        data = []

        for file in tqdm(os.listdir(self.data_path), desc = "Loading procedures..."):
            file_path = os.path.join(self.data_path, file)
            loader = TextLoader(file_path = file_path, encoding = "utf-8")
            documents = loader.load()
            for doc in documents:
                data.append(doc.page_content)
        
        texts = self.text_splitter.create_documents(data)
        return texts
    
data_loader = DataLoader()
