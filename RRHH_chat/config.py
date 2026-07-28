from dotenv import load_dotenv
import os

load_dotenv()

DOCUMENT_PATH = "documentos"

VECTORSTORE_PATH = "vectorstore"

CHUNK_SIZE = 300
CHUNK_OVERLAP = 30

EMBEDDING_MODEL = "models/gemini-embedding-001"

LLM_MODEL = "gemini-2.5-flash"

TEMPERATURE = 0.2

SCORE_THRESHOLD = 0.3

TOP_K = 4

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
