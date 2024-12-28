from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_vector_store(texts: list[str]) -> FAISS:
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.create_documents(texts)
    return FAISS.from_documents(documents, embeddings)
