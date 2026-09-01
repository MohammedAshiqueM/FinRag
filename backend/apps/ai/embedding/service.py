from backend.apps.ai.embedding.factory import get_embedding_service
from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk


class EmbeddingService:
    """
    Service layer for embedding operations.

    This class abstracts the underlying embedding provider and exposes
    methods to generate embeddings for:
        - Document chunks (for storage in a vector database).
        - User queries (for retrieval against stored embeddings).

    By separating chunk and query embeddings, the service provides a
    consistent interface while allowing different providers to be swapped
    in transparently.
    """

    def __init__(self, provider=None):
        self.provider = provider or get_embedding_service()

    def embed_chunks(
        self,
        chunks: list[Chunk],
    ) -> list[list[float]]:

        texts = [chunk.text for chunk in chunks]

        if not texts:
            return []

        return self.provider.embed_chunks(texts)
    
    
    def embed_query(self, query):

        return self.provider.embed_query(query)