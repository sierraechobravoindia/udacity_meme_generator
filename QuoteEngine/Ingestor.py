from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from .DOCXIngestor import DOCXIngestor
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor

class Ingestor(IngestorInterface):
    """Convert a file with Dog Quotes to a List of QuoteModel
    
    takes files of type .docx, .csv, .txt, .pdf
    """
    ingestors = [DOCXIngestor, CSVIngestor, TXTIngestor, PDFIngestor]
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)