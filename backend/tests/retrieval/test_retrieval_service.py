
from backend.apps.retrieval.services.retrieval_services import RetrievalService
from backend.apps.ai.vectorstore.retrieved_chunks import RetrievedChunk


class FakeEmbeddingService:

    def embed_query(self, query):
        return [0.1, 0.2, 0.3]
    
class FakeVectorStore:

    def similarity_search(
        self,
        query_embedding,
        k=5,
        filters=None,
    ):
        return [
            RetrievedChunk(
                id="chunk_1",
                text="Apple faces supply chain risks.",
                metadata={
                    "company": "Apple",
                    "page": 10,
                },
                score=0.95,
            )
        ]
        
service = RetrievalService(
    embedding_service=FakeEmbeddingService(),
    vector_store=FakeVectorStore(),
)

results = service.retrieve(
    "What risks does Apple face?"
)

for result in results:
    print(result.text)