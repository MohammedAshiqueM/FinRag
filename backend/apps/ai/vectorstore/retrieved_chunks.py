from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    """
    Standardized representation Retrieved Chunk
    
    This object encapsulates the result of a similarity search from the
    vector store. All vector database implementations should return
    instances of this class.
    """
    id: str
    text: str
    metadata: dict
    score: float