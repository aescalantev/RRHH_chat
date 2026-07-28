from langchain_google_genai import ChatGoogleGenerativeAI

from config import LLM_MODEL,TEMPERATURE,GEMINI_API_KEY


def obtener_llm():

    return ChatGoogleGenerativeAI(

        model=LLM_MODEL,

        temperature=TEMPERATURE,

        google_api_key=GEMINI_API_KEY

    )