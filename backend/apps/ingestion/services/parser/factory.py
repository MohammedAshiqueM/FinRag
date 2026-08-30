from backend.apps.ingestion.services.parser.pdf_parser import PDFParser

PARSERS = {
    "pdf": PDFParser,
    # "docx": DocxParser,
    # "txt": TextParser,
}

def get_parser(extention: str):
    """
    Factory function that returns the appropriate parser 
    based on PARSER_PROVIDER configuration.
    """
    parser_class = PARSERS.get(extention.lower())
    if parser_class is None:
        raise ValueError(f"unknown file extention {extention}")
    return parser_class()
    