from backend.apps.ai.keyword.factory import get_keyword_retriever
from backend.apps.ai.vectorstore.factory import get_vector_store_service
from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk
from backend.apps.ai.embedding.embedding_service import EmbeddingService



class IndexingService:
    """
    Service layer responsible for embedding text chunks and indexing them
    into a vector store for similarity search and retrieval.
    """
    def __init__(
        self,
        embedding_service=None,
        vector_store=None,
        keyword_service=None,
    ):
        self.embedding_service = (
            embedding_service or EmbeddingService()
        )

        self.vector_store = (
            vector_store or get_vector_store_service()
        )
        
        self.keyword_service = (
            keyword_service or get_keyword_retriever()
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
        
        self.keyword_service.index(chunks)