from backend.apps.ai.vectorstore.retrieved_chunks import RetrievedChunk


class RetrievalService:
    """
    Service layer for semantic retrieval of top-k text chunks.

    Attributes:
        embedding_service: Abstract embedding service used to generate query embeddings.
        vector_store: Abstract vector storage layer that supports similarity search operations.
    """

    def retrieve(
        self,
        query: str,
        k: int = 5,
        filters: dict | None = None,
    ) -> list[RetrievedChunk]:

        query_embedding = self.embedding_service.embed_query(query)

        results = self.vector_store.similarity_search(
            query_embedding=query_embedding,
            k=k,
            filters=filters,
        )

        return results