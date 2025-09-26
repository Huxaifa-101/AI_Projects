from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 1️⃣ Initialize the embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2️⃣ Load an existing Chroma vector store from disk
vectordb = Chroma(persist_directory="data/chroma_db", embedding_function=embeddings)

# 3️⃣ Convert the vector store into a retriever
retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k":1})

# 4️⃣ Example queries
query = "What are the prerequisites for HUM 320?"
query_1 = "What's the weather in Karachi?"  # this will likely not match any document

# 5️⃣ Retrieve relevant documents for the query
results = retriever.get_relevant_documents(query)

# 6️⃣ Print the contents of the top matching document(s)
for r in results:
    print("----")
    print(r.page_content)
