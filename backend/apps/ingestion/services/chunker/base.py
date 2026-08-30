from abc import ABC, abstractmethod

from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk


class BaseChunker(ABC):
    
    @abstractmethod
    def chunk(self, pages:list[str]) -> list[Chunk]:
        pass