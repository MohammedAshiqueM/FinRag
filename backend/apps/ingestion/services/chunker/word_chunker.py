from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk


class WordChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, pages: list[str]) -> list[Chunk]:

        chunks = []

        for page_number, page_text in enumerate(pages, start=1):

            words = page_text.split()

            start = 0

            while start < len(words):

                end = start + self.chunk_size

                chunk_text = " ".join(words[start:end]).strip()

                if chunk_text:
                    chunks.append(
                        Chunk(
                            text=chunk_text,
                            metadata={
                                "page": page_number,
                                "chunk_index": len(chunks),
                            },
                        )
                    )

                start += self.chunk_size - self.overlap

        return chunks