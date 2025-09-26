from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def get_course_retriever(k: int = 20):
    """
    Return a retriever for the course catalog.

    Uses a Chroma vector store (previously built from .docx course documents)
    and HuggingFace embeddings to find the most relevant course info.

    Args:
        k (int): number of top results to return for a query (default 20)

    Returns:
        Retriever object with `.get_relevant_documents(query)` method
    """
    # initialize embeddings model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # load the existing Chroma DB containing course embeddings
    vectordb = Chroma(
        persist_directory="data/chroma_db",
        embedding_function=embeddings
    )

    # convert the vector store into a retriever with similarity search
    # 'k' controls how many top matches are returned
    return vectordb.as_retriever(search_type="similarity", search_kwargs={"k": k})
