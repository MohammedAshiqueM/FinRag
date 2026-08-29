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
    
    def embed(self, texts):
        """
        Generate embeddings for the given texts.
        """
        embeddings = self.model.encode(
            texts,
            convert_to_numpy = True
        )
        return embeddings.tolist()