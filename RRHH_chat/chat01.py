
# %%
# !pip install -q \
#     langchain --no-cache-dir \
#     langchain-google-genai \
#     google-generativeai \
#     langchain_community \
#     faiss-cpu \
#     langchain-text-splitters \
#     pymupdf \
#     langgraph

# %%
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

# %%
# print(len(docs))

# %% [markdown]
# **Dividir el texto**

# %%
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
docs_splits = splitter.split_documents(docs)

# %% [markdown]
# **Crear Embeddings**

# %%
from google.colab import userdata

GEMINI_API_KEY=userdata.get("GEMINI_API_KEY")

# %%
from langchain_google_genai import GoogleGenerativeAIEmbeddings

modelo_embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001",
    google_api_key=GEMINI_API_KEY
)

# %%
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(docs_splits, modelo_embeddings)

retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.3, "k": 4}
)

vectorstore.save_local("vectorstore")

# %%
from langchain_community.vectorstores import FAISS

vectorstore = FAISS.from_documents(docs_splits, modelo_embeddings)

retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.3, "k": 4}
)

# %%
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key=GEMINI_API_KEY
)

# %%
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

prompt_rag = ChatPromptTemplate(
    [
        ("system",
            """Eres el especialista en RR.HH. de la empresa Excelence Desarrollo de Software.
            Responde siempre utilizando los conocimientos del contexto que te fue pasado a ti.
            Si no hay informacion sobre la pregunta en los datos, responde solo 'No lo se'.
            """
        ),
        ("human", "Contexto: {context}\nPregunta del empleado: {input}")
    ]
)

# Helper function to format documents for stuffing into the prompt
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Re-implement create_stuff_documents_chain functionality using LCEL
document_chain = (
    {
        "context": lambda x: format_docs(x["context"]), # Takes list of docs, formats to string
        "input": RunnablePassthrough() # Passes the original 'input' through
    }
    | prompt_rag
    | llm
    | StrOutputParser()
)

# %%
#def consultar(pregunta):
pregunta = "Que es RAG?"
documentos = retriever.invoke(pregunta)

contexto = "\n\n".join(
    [d.page_content for d in documentos]
)

mensajes = prompt_rag.format_messages(
    context=contexto,
    input=pregunta
)

respuesta = llm.invoke(mensajes)

return respuesta.content

# %%
while True:

    p = input("Pregunta: ")

    if p=="salir":
        break

    print(consultar(p))


