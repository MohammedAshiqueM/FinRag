class VectorStoreError(Exception):
    """Base exception for vector store errors."""


class CollectionNotFoundError(VectorStoreError):
    """Raised when a collection doesn't exist."""


class DuplicateDocumentError(VectorStoreError):
    """Raised when duplicate IDs are added."""


class SearchError(VectorStoreError):
    """Raised when similarity search fails."""