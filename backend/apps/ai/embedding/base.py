from abc import ABC, abstractmethod


class BaseEmbedding(ABC):
    """
    Abstract Base Class that defines the interface for all embedding providers.
    
    Any concrete embedding service (like SentenceTransformerEmbedding or OpenAIEmbedding)
    must implement the `embed()` method as defined here.
    """
    @abstractmethod
    def embed(self, texts:list[str]) -> list[list[float]]:
        """
        Convert a list of texts into embeddings (vectors).
        
        Args:
            texts: List of strings to be embedded
            
        Returns:
            List of embeddings, where each embedding is a list of floats
        """
        pass