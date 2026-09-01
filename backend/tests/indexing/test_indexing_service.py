from backend.apps.ai.indexing.services.indexing_service import IndexingService
from backend.apps.ingestion.services.chunker.parsed_chunk import Chunk


class FakeVectorStore:

    def __init__(self):
        self.documents = []

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas,
    ):
        self.documents.extend(
            zip(
                ids,
                documents,
                embeddings,
                metadatas,
            )
        )
        
class FakeEmbeddingService:

    def embed_chunks(self, chunks):

        return [
            [0.1, 0.2, 0.3]
            for _ in chunks
        ]

chunks = [
    Chunk(
        id="1_0",
        text="Apple reported strong revenue.",
        metadata={
            "document_id": 1,
            "page": 1,
            "chunk_index": 0,
        },
    ),
    Chunk(
        id="1_1",
        text="Apple faces supply chain risks.",
        metadata={
            "document_id": 1,
            "page": 2,
            "chunk_index": 1,
        },
    ),
]

service = IndexingService(
    embedding_service=FakeEmbeddingService(),
    vector_store=FakeVectorStore(),
)

service.index(chunks)

print(service.vector_store.documents)