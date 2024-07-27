# from langchain.vectorstores import Chroma
# import chromadb
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

loader = TextLoader("data/test.txt")
document = loader.load()
# print(document)

text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = text_splitter.split_documents(document)
# print(chunks[:2])
# chunks_with_ids = [{"id": f"chunk_{i}", "text": chunk} for i, chunk in enumerate(chunks)]
# print("-----")
# print(chunks_with_ids[:2])


# for doc in chunks_with_ids:
#     print(doc["text"].page_content)
#     print("   -----------  ")

# embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
embedding_function = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
# print(embedding_function)

# db = Chroma.from_documents(docs, embedding_function)
# db = Chroma.from_documents(docs, embedding_function, persist_directory="chroma")

# query = "what is the meaning of life?"
# docs = db.similarity_search(query)
# print(embedding_function)

# embeddings = embedding_function.get_text_embedding("cat")
# embeddings = embedding_function.embed_documents([doc["text"].page_content for doc in chunks_with_ids])
# print(len(embeddings))
# print(embeddings[:100])

# chroma_store = Chroma()
# chroma_store.add_documents(docs, embedding=embedding_function)


# Initialize the Chroma client
# client = chromadb.Client()

# Create or load a collection
# This code snippet is creating a collection in a Chroma database using the `chromadb` library. Here's
# a breakdown of what each part of the code is doing:
# collection_name = "col1"
# collection = client.create_collection(name=collection_name)
# ids = [doc["id"] for doc in chunks_with_ids]
# texts = [doc["text"] for doc in chunks_with_ids]
# embedding_vectors = embeddings
# metadata = [{} for _ in chunks_with_ids]

# collection.upsert(
#     ids=ids,
#     embeddings=embedding_vectors
#     # metadata=metadata
# )

db = Chroma.from_documents(chunks, embedding_function)
query = "what did Alice say"
docs = db.similarity_search(query)


print(docs[0].page_content)