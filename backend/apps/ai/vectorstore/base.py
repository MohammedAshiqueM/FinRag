from abc import ABC, abstractmethod
from typing import Any, Dict



class BaseVectorStore(ABC):
    """
    Abstract Base Class that defines the interface for all vector storage providers.
    
    Any concrete vector storage service (like ChromaVectorStore, PgVectorStore, Pinecone, etc.)
    must implement the methods defined here.
    """
    @abstractmethod
    def add_documents(
            self,
            documents: list[str],
            metadatas: list[Dict[str, Any]],
            embeddings: list[list[float]],
            ids: list[str] | None = None
            ) -> None:
        """Add documents to the vector store."""
        pass
    
    @abstractmethod
    def similarity_search(
        self,
        query_embedding: list[float],
        k: int = 5,
        filters: dict | None = None
        ) -> dict:
        """Search for similar documents."""
        pass
    
    @abstractmethod
    def delete_documents(self, filters: dict) -> None:
        """Delete documents based on filters."""
        pass