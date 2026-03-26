from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_vector_db():
    return FAISS.load_local("faiss_index", OpenAIEmbeddings())