from backend.apps.ingestion.services.chunker.word_chunker import WordChunker
from backend.finrag import settings


def get_chunker():
    chunker = settings.CHUNKER
    
    if chunker == 'word':
        return WordChunker()
    
    raise ValueError(f"unknown parser {chunker}")