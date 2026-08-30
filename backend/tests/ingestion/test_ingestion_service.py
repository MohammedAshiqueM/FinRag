import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "backend.finrag.settings"
)

import django

django.setup()

from pathlib import Path

from backend.apps.ingestion.services.chunker.factory import get_chunker
from backend.apps.ingestion.services.cleaner.cleaner import TextCleaner
from backend.apps.ingestion.services.ingestion_service import IngestionService
from backend.apps.ingestion.services.metadata.enricher import MetadataEnricher
from backend.apps.ingestion.services.parser.factory import get_parser

parser = get_parser('pdf')
cleaner = TextCleaner()
chunker = get_chunker()
metadata_enricher = MetadataEnricher()

service = IngestionService(
    parser=parser,
    cleaner=cleaner,
    chunker=chunker,
    metadata_enricher=metadata_enricher,
)

BASE_DIR = Path(__file__).resolve().parent.parent

PDF_PATH = (
    BASE_DIR
    / "fixtures"
    / "documents"
    / "sample.pdf"
)

print("path is ",PDF_PATH)
print("path exists: ",PDF_PATH.exists())


chunks = service.ingest(
    file_path=PDF_PATH,
    document_id=1,
    document_metadata={
        "title": "Sample Document",
        "source": "test",
    },
)
print("Total chunks:", len(chunks))

for chunk in chunks[:5]:
    print("=" * 80)
    print("ID:", chunk.id)
    print("Metadata:", chunk.metadata)
    print("Text:", chunk.text)