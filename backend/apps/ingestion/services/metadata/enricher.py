from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk


class MetadataEnricher:
    """
    Adding chunk metadata and document metadata to entriched metadata
    """
    def enrich(
        self,
        chunks: list[Chunk],
        document_id: int,
        document_metadata: dict,
    ) -> list[Chunk]:

        enriched_chunks = []

        for chunk in chunks:
            
            chunk_id = f"{document_id}_{chunk.metadata['chunk_index']}"

            metadata = {
                **document_metadata,
                **chunk.metadata,
            }

            enriched_chunks.append(
                Chunk(
                    id=chunk_id,
                    text=chunk.text,
                    metadata=metadata,
                )
            )

        return enriched_chunks