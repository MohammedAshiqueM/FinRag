from pathlib import Path
from unittest import result

from backend.apps.ai.vectorstore.retrieved_chunks import RetrievedChunk
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
    
    def similarity_search(
        self,
        query_embedding,
        k=5,
        filters=None
    ) -> list[RetrievedChunk]:

        result = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            where=filters
        )

        retrieved_chunks = []

        for i in range(len(result["ids"][0])):
            retrieved_chunks.append(
                RetrievedChunk(
                    id=result["ids"][0][i],
                    text=result["documents"][0][i],
                    metadata=result["metadatas"][0][i],
                    score=result["distances"][0][i],
                )
            )

        return retrieved_chunks
    
    def delete_documents(self, filters):
        """Delete documents matching the filters."""
        self.collection.delete(
            where=filters
        )