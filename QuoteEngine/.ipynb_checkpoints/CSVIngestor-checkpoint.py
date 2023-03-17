import pandas
from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class CSVIngestor(IngestorInterface):
    """Convert a csv file with Dog Quotes to a List of QuoteModel"""
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        
        quotes = []
        df = pandas.read_csv(path, header=0)
        
        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
                        
        return quotes
          