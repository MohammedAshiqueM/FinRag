from backend.finrag.settings import KEYWORD_RETRIEVER_PROVIDER

from .base import BaseKeywordRetriever
from .providers.bm25 import BM25KeywordRetriever





def get_keyword_retriever() -> BaseKeywordRetriever:

    if KEYWORD_RETRIEVER_PROVIDER == "bm25":
        return BM25KeywordRetriever()

    raise ValueError(
        f"Unknown keyword retriever provider: "
        f"{KEYWORD_RETRIEVER_PROVIDER}"
    )