from backend.apps.ai.vectorstore.factory import get_vector_store_service
from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk
from backend.apps.ai.embedding.service import EmbeddingService



class IndexingService:

    def __init__(
        self,
        embedding_service=None,
        vector_store=None,
    ):
        self.embedding_service = (
            embedding_service or EmbeddingService()
        )

        self.vector_store = (
            vector_store or get_vector_store_service()
        )

    def index(
        self,
        chunks: list[Chunk],
    ) -> None:

        if not chunks:
            return

        embeddings = self.embedding_service.embed_chunks(chunks)

        if len(chunks) != len(embeddings):
            raise ValueError(
                "Number of chunks and embeddings must match"
            )

        self.vector_store.add_documents(
            ids=[chunk.id for chunk in chunks],
            documents=[chunk.text for chunk in chunks],
            embeddings=embeddings,
            metadatas=[chunk.metadata for chunk in chunks],
        )