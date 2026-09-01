from pathlib import Path


class IngestionService:
    """
    High-level ingestion pipeline that orchestrates all ingestion steps.

    Workflow:
        1. Parse the document into raw text and pages.
        2. Clean the extracted text.
        3. Chunk the cleaned text into smaller segments.
        4. Enrich each chunk with metadata.

    Returns:
        A list of enriched chunks ready for downstream processing (e.g., embedding, storage).
    """

    def __init__(
        self,
        parser,
        cleaner,
        chunker,
        metadata_enricher,
    ):
        self.parser = parser
        self.cleaner = cleaner
        self.chunker = chunker
        self.metadata_enricher = metadata_enricher

    def ingest(
        self,
        file_path: str | Path,
        document_id: int,
        document_metadata: dict,
    ):

        # 1. Parse
        parsed_document = self.parser.parse(file_path)

        # 2. Clean
        cleaned_pages = [
            self.cleaner.clean(page)
            for page in parsed_document.pages
        ]

        # 3. Chunk
        chunks = self.chunker.chunk(cleaned_pages)

        # 4. Enrich metadata
        enriched_chunks = self.metadata_enricher.enrich(
            chunks=chunks,
            document_id=document_id,
            document_metadata=document_metadata,
        )

        return enriched_chunks