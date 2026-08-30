from backend.apps.ai.vectorstore.chroma import ChromaVectorStore
from backend.finrag import settings


def get_vector_store_service():
    """
    Factory function that returns the appropriate vector db
    based on the VECTOR_DB from settings.
    """
    
    provider = settings.VECTOR_DB
    
    if provider == "chromadb":
        return ChromaVectorStore()
    
    raise ValueError(f"unknown vector db provider: {provider}")