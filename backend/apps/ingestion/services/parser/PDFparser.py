import PyPDF2
from backend.apps.ingestion.services.parser.base import BaseParser

class PDFParser(BaseParser):
    """
    Concrete implementation for parsing PDF files using PyPDF2.
    """
    def extract_text(self, file):
        """
        Extract text from a PDF file.
        """
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Error extracting PDF text: {str(e)}")