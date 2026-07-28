from langchain_core.prompts import ChatPromptTemplate

PROMPT_RAG = ChatPromptTemplate([

("system",

"""Eres el especialista en RRHH.

Responde únicamente utilizando el contexto.

Si no existe información responde solamente:

No lo sé.

"""),

("human",

"Contexto:\n{context}\n\nPregunta:\n{input}")

])