from dataclasses import dataclass
from typing import Any, Dict, List, Optional

@dataclass
class ParsedDocument:
    """
    Standardized representation of a parsed doc
    All parser should return this object.
    """
    text:str                            #full extract text
    pages:List[str]                     #Text per page(useful for chunking)
    metadata:Dict[str, Any]             #File info, source etc
    chunk:Optional[List[str]] = None    #optional pre-chunked text
    
    def __post_init__(self):
        if self.chunk is None:
            self.chunk = []
            
# Above I used data class which can represend in actual class like below

# class ParsedDocument:
#     def __init__(self, 
#                  text: str, 
#                  pages: List[str], 
#                  metadata: Dict[str, Any],
#                  chunks: Optional[List[str]] = None):
#         self.text = text
#         self.pages = pages
#         self.metadata = metadata
#         self.chunks = chunks or []