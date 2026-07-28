from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import EMBEDDING_MODEL, GEMINI_API_KEY


def obtener_embeddings():

    return GoogleGenerativeAIEmbeddings(

        model=EMBEDDING_MODEL,

        google_api_key=GEMINI_API_KEY

    )