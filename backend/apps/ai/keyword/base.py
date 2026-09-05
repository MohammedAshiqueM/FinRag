from abc import ABC, abstractmethod

from backend.apps.ai.vectorstore.retrieved_chunks import RetrievedChunk
from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk


class BaseKeywordRetriever(ABC):

    @abstractmethod
    def index(self, chunks: list[Chunk]) -> None:
        """
        Index chunks for keyword retrieval.
        """
        pass

    @abstractmethod
    def search(
        self,
        query: str,
        k: int = 5,
        filters: dict | None = None,
    ) -> list[RetrievedChunk]:
        """
        Search indexed chunks using keyword-based retrieval.
        """
        pass

    @abstractmethod
    def delete(self, filters: dict | None = None) -> None:
        """
        Delete indexed chunks.
        """
        pass