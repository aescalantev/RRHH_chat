from chatbot.vector_db import obtener_retriever
from chatbot.prompts import PROMPT_RAG
from chatbot.llm import obtener_llm


retriever = obtener_retriever()

llm = obtener_llm()


def consultar(pregunta):

    documentos = retriever.invoke(pregunta)

    contexto = "\n\n".join(

        doc.page_content

        for doc in documentos

    )

    mensajes = PROMPT_RAG.format_messages(

        context=contexto,

        input=pregunta

    )

    respuesta = llm.invoke(mensajes)

    return respuesta.content