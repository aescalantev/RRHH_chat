from chatbot.loaders import cargar_documentos
from chatbot.splitter import dividir_documentos
from chatbot.vector_db import crear_vectorstore


docs = cargar_documentos()

chunks = dividir_documentos(docs)

crear_vectorstore(chunks)

print("Vectorstore creado correctamente.")

