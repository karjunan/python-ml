from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function_llama():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings