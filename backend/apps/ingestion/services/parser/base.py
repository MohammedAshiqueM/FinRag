from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Abstract Base Class for document parsers.
    
    Any concrete parser (PDFParser, DocxParser, etc.) must implement 
    the `extract_text` method.
    """
    @abstractmethod
    def parse(self, file: str) -> str:
        """
        Extract text from a document file.
        
        Args:
            file_path: Path to the document file
            
        Returns:
            Extracted text as string
        """
        pass