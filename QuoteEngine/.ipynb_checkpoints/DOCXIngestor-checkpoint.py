from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import docx

class DOCXIngestor(IngestorInterface):
    """Convert a docx file with Dog Quotes to a List of QuoteModel"""
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
            
        quotes = []
        doc = docx.Document(path)
        
        for p in doc.paragraphs:
            if p.text != "":
                parsed = p.text.split('-')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)
            
        return quotes