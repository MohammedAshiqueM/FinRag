from pathlib import Path

import pymupdf
from django.utils import timezone

from backend.apps.ingestion.services.parser.parsed_document import ParsedDocument
from backend.apps.ingestion.services.parser.base import BaseParser
from backend.apps.ingestion.services.parser.exceptions import ParserError


class PDFParser(BaseParser):
    """
    Parser for PDF files,
    It extracts the data from the file using PyMuPDF, return text, metadata, pages as object of ParsedDocument
    """
    def parse(self, file_path: str | Path) -> ParsedDocument:

        file_path = Path(file_path)

        try:
            with pymupdf.open(file_path) as document:

                pages = []
                full_text_parts = []

                for page in document:
                    page_text = page.get_text("text") or ""

                    pages.append(page_text)
                    full_text_parts.append(page_text)

                metadata = {
                    "filename": file_path.name,
                    "file_type": "pdf",
                    "num_pages": len(pages),
                    "parsed_at": timezone.now().isoformat(),
                }

                return ParsedDocument(
                    text="\n".join(full_text_parts).strip(),
                    pages=pages,
                    metadata=metadata,
                )

        except Exception as e:
            raise ParserError(
                f"Failed to parse PDF: {file_path}"
            ) from e