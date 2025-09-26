import sys, os
# add parent dir to path for local imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_community.document_loaders import Docx2txtLoader   # load .docx text
from langchain.text_splitter import RecursiveCharacterTextSplitter # split into chunks
from langchain_community.vectorstores import Chroma               # vector store
from langchain_huggingface import HuggingFaceEmbeddings           # HF embeddings

# dirs
folder_path = "data/raw"       # input docs
persist_dir = "data/chroma_db" # chroma db location

# load all .docx docs
all_docs = []
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".docx"):
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        loader = Docx2txtLoader(file_path)
        docs = loader.load()          # returns list[Document]
        all_docs.extend(docs)

print(f"Loaded {len(all_docs)} documents from {folder_path}")

# split into chunks (800 chars, 100 overlap)
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(all_docs)
print(f"Split into {len(chunks)} chunks")

# embed + store in chroma
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectordb = Chroma.from_documents(
    chunks,
    embedding=embeddings,
    persist_directory=persist_dir
)
vectordb.persist()

print(f"Indexed {len(chunks)} chunks into ChromaDB at {persist_dir}")
