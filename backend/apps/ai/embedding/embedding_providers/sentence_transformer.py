from backend.apps.ai.embedding.base import BaseEmbedding
from backend.finrag.settings import EMBEDDING_MODEL
from sentence_transformers import SentenceTransformer

class SentenceTransformerEmbedding(BaseEmbedding):
    """
    Concrete implementation of BaseEmbedding using Sentence Transformers.
    
    This class is responsible for loading the model and generating embeddings
    using the SentenceTransformer library.
    """
    def __init__(self):
        """
        Initialize the SentenceTransformer model.
        """
        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )
    
    def embed_chunks(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for a list of chunk texts.

        Args:
            texts (list[str]): List of chunk strings (e.g., 500-word segments).

        Returns:
            list[list[float]]: Embedding vectors for each chunk, suitable for
            storage in a vector database.
        """
        embeddings = self.model.encode(
            texts,
            convert_to_numpy = True
        )
        return embeddings.tolist()
    
    def embed_query(self, query: str) -> list[float]:
        """
        Generate an embedding for a single user query.

        Args:
            query (str): The query string.

        Returns:
            list[float]: Embedding vector for the query, used for retrieval
            against stored chunk embeddings.
        
        Note:
            Although the logic is similar to `embed_chunks`, this method is
            separated for semantic clarity and abstraction.
        """
        embedding = self.model.encode(
            query,
            convert_to_numpy=True,
        )

        return embedding.tolist()