from backend.apps.ai.vectorstore.retrieved_chunks import RetrievedChunk
from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk

from .base import BaseKeywordRetriever
from .factory import get_keyword_retriever


class KeywordRetrievalService:
    """
    Service layer for keyword retrieval of top-k text chunks.
    """
    def __init__(
        self,
        retriever: BaseKeywordRetriever | None = None,
    ):
        self.retriever = retriever or get_keyword_retriever()

    def index(
        self,
        chunks: list[Chunk],
    ) -> None:

        self.retriever.index(chunks)

    def search(
        self,
        query: str,
        k: int = 5,
        filters: dict | None = None,
    ) -> list[RetrievedChunk]:

        return self.retriever.search(
            query=query,
            k=k,
            filters=filters,
        )

    def delete(
        self,
        filters: dict | None = None,
    ) -> None:

        self.retriever.delete(filters=filters)