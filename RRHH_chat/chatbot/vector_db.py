from langchain_community.vectorstores import FAISS
import os
from config import VECTORSTORE_PATH
from chatbot.embeddings import obtener_embeddings


def crear_vectorstore(chunks):

    embeddings = obtener_embeddings()

    db = FAISS.from_documents(chunks, embeddings)
    
    # ruta_archivo = os.path.abspath(__file__)
    # directorio_archivo = os.path.dirname(ruta_archivo)
    # print("Directorio donde está el archivo:", directorio_archivo)
    # input()

    db.save_local(VECTORSTORE_PATH)


def cargar_vectorstore():

    embeddings = obtener_embeddings()
    
    # ruta_archivo = os.path.abspath(__file__)
    # directorio_archivo = os.path.dirname(ruta_archivo)
    # print("Directorio donde está el archivo:", directorio_archivo)
    # input()
    
    return FAISS.load_local(

        VECTORSTORE_PATH,

        embeddings,

        allow_dangerous_deserialization=True

    )


def obtener_retriever():

    db = cargar_vectorstore()

    return db.as_retriever(

        search_type="similarity_score_threshold",

        search_kwargs={

            "score_threshold":0.3,

            "k":4

        }

    )