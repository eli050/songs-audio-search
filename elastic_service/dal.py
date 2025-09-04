from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class DataAccessLayer:
    """Data Access Layer for Elasticsearch operations."""
    def __init__(self, es_client:Elasticsearch, index_name: str,mapping:dict=None):
        self.es_client = es_client
        self.index_name = index_name
        if mapping is not None:
            self.mapping = mapping
        else:
            self.mapping = DataAccessLayer._get_mapping()
        self._create_index()

    def _create_index(self):
        """Create the Elasticsearch index if it doesn't exist."""
        if not self.es_client.indices.exists(index=self.index_name):
            self.es_client.indices.create(index=self.index_name,mappings=self.mapping)
            print(f"Index '{self.index_name}' created.")
        else:
            print(f"Index '{self.index_name}' already exists.")

    @staticmethod
    def _get_mapping():

        return {
            "properties": {
                "song_id": {
                    "type": "keyword"
                },
                "title": {
                    "type": "text"
                },
                "artist": {
                    "type": "text"
                },
                "lyrics": {
                    "type": "text"
                }
            }
        }