"""
Embedding service architecture for scalability and separation of concerns.

Components:
    - Provider: Concrete implementations of BaseEmbedding (e.g., SentenceTransformer, Word2Vec).
    - Factory: The get_embedding_service function, which selects the appropriate provider.
    - Service: The EmbeddingService class, which exposes a clean interface for chunk and query embeddings.

Extension:
    To add a new embedding provider, inherit from BaseEmbedding and update the factory method.

Note:
    This layered architecture is consistently applied across other modules such as LLM, vectorstore,
    chunker, and parser services.
"""
