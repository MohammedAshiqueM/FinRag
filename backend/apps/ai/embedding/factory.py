from backend.apps.ai.embedding.sentence_transformer import SentenceTransformerEmbedding
from backend.finrag.settings import EMBEDDING_PROVIDER


def get_embedding_service():
    """
    Factory function that returns the appropriate embedding service 
    based on the EMBEDDING_PROVIDER configuration.
    
    This allows us to easily switch between different embedding providers
    without changing the business logic.
    """
    provider = EMBEDDING_PROVIDER
    
    if provider == "sentence-transformers":
        return SentenceTransformerEmbedding()

    raise ValueError(f"unknown provider {provider}")