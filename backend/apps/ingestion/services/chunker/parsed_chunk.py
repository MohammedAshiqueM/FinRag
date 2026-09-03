from dataclasses import dataclass
from typing import Any


@dataclass
class Chunk:
    """
    Standardized representation of a Chunk
    
    This object encapsulates a unit of text produced by a chunking method
    before embedding and indexing. All chunking strategies should return
    instances of this class.
    """
    text: str
    metadata: dict[str, Any]
    id: str | None = None