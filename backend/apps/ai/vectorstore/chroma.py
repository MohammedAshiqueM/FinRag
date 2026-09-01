from pathlib import Path
from unittest import result

import chromadb
from backend.apps.ai.vectorstore.base import BaseVectorStore

CHROMA_DB_PATH = Path(__file__).parent.parent / "chroma_db"

CHROMA_DB_PATH.mkdir(exist_ok=True)

class ChromaVectorStore(BaseVectorStore):
    """
    Concrete implementation of BaseVectorStore using chromadb.
    
    This class is responsible for loading the model and generating prompt result
    using the chromadb.
    """
    
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_PATH)
        )
        self.collection = self.client.get_or_create_collection(
            name="financial_documents"
        )
        
    def add_documents(self, documents, metadatas, ids, embeddings):
        """Add documents with metadata to the collection."""
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings,
            ids=ids
        )
    
    def similarity_search(self, query_embedding, k=5, filters=None):
        """Perform similarity search."""
        result = self.collection.query(
            query_embeddings=[query_embedding],
            n_result=k,
            where=filters
        )
        
        return result
    
    def delete_documents(self, filters):
        """Delete documents matching the filters."""
        self.collection.delete(
            where=filters
        )