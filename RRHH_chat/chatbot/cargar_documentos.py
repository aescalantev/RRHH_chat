from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

docs = []

for documento in Path("/content/").glob("*.pdf"):
    try:
        loader = PyMuPDFLoader(str(documento))
        docs.extend(loader.load())
        print(f"Archivo cargado: {documento.name}")
    except Exception as e:
        print(f"Error cargando archivo: {documento.name}: {e}")

# print(f"Total de documentos cargados: {len(docs)}")

# print(len(docs))

# **Dividir el texto**

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
docs_splits = splitter.split_documents(docs)

# **Crear Embeddings**

from google.colab import userdata

GEMINI_API_KEY=userdata.get("GEMINI_API_KEY")


from langchain_google_genai import GoogleGenerativeAIEmbeddings

modelo_embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001",
    google_api_key=GEMINI_API_KEY
)


from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(docs_splits, modelo_embeddings)

retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.3, "k": 4}
)

vectorstore.save_local("vectorstore")

