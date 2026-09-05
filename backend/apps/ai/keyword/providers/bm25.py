from backend.apps.ai.vectorstore.retrieved_chunks import RetrievedChunk
from rank_bm25 import BM25Okapi

from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk

from ..base import BaseKeywordRetriever


class BM25KeywordRetriever(BaseKeywordRetriever):
    """
    Keyword indexing and retrieval using BM25.
    
    Intended for development use only. 
    This service is not production-ready, as keyword indexes 
    are stored entirely in memory.
    """
    def __init__(self):
        self.bm25 = None
        self.chunks: list[Chunk] = []

    def index(self, chunks: list[Chunk]) -> None:

        if not chunks:
            return

        self.chunks = chunks

        tokenized_documents = [
            self._tokenize(chunk.text)
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(tokenized_documents)

    def search(
        self,
        query: str,
        k: int = 5,
        filters: dict | None = None,
    ) -> list[RetrievedChunk]:

        if self.bm25 is None:
            return []

        query_tokens = self._tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        ranked_indexes = sorted(
            range(len(scores)),
            key=lambda index: scores[index],
            reverse=True,
        )

        results = []

        for index in ranked_indexes:

            chunk = self.chunks[index]

            if filters and not self._matches_filters(
                chunk,
                filters,
            ):
                continue

            results.append(
                RetrievedChunk(
                    id=chunk.id,
                    text=chunk.text,
                    metadata=chunk.metadata,
                    score=float(scores[index]),
                )
            )

            if len(results) >= k:
                break

        return results

    def delete(self, filters: dict | None = None) -> None:

        if filters is None:
            self.bm25 = None
            self.chunks = []
            return

        remaining_chunks = [
            chunk
            for chunk in self.chunks
            if not self._matches_filters(chunk, filters)
        ]

        self.index(remaining_chunks)

    def _tokenize(self, text: str) -> list[str]:
        return text.lower().split()

    def _matches_filters(
        self,
        chunk: Chunk,
        filters: dict,
    ) -> bool:

        for key, expected_value in filters.items():

            actual_value = chunk.metadata.get(key)

            if actual_value != expected_value:
                return False

        return True