from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

from config import DOCUMENT_PATH


def cargar_documentos():

    docs=[]

    for documento in Path(DOCUMENT_PATH).glob("*.pdf"):

        loader = PyMuPDFLoader(str(documento))

        docs.extend(loader.load())

    return docs