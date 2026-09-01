import os
from pathlib import Path

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "backend.finrag.settings"
)

import django
django.setup()

from backend.apps.ingestion.services.parser.factory import get_parser

def main():
    # Get the PDF parser
    parser = get_parser("pdf")

    # Resolve the sample PDF path
    BASE_DIR = Path(__file__).resolve().parent.parent
    PDF_PATH = BASE_DIR / "fixtures" / "documents" / "sample.pdf"

    print("PDF path:", PDF_PATH)
    print("Path exists:", PDF_PATH.exists())

    try:
        parsed_doc = parser.parse(PDF_PATH)

        print("=" * 80)
        print("FILENAME:", parsed_doc.metadata.get("filename"))
        print("FILE TYPE:", parsed_doc.metadata.get("file_type"))
        print("NUM PAGES:", parsed_doc.metadata.get("num_pages"))
        print("PARSED AT:", parsed_doc.metadata.get("parsed_at"))
        print("=" * 80)
        print("FULL TEXT (preview):")
        print(parsed_doc.text[:500], "...")  # show first 500 chars
        print("=" * 80)
        print("PAGE TEXTS:")
        for i, page in enumerate(parsed_doc.pages, start=1):
            print(f"--- Page {i} ---")
            print(page[:200], "...")  # show first 200 chars per page

    except Exception as e:
        print("Parser failed:", str(e))


if __name__ == "__main__":
    main()
