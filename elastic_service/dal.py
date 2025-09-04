from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class DataAccessLayer:
    """Data Access Layer for Elasticsearch operations."""
    def __init__(self, es_client:Elasticsearch, index_name: str,mapping:dict = None):
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
                },
                "link": {
                    "type": "keyword"
                }
            }
        }
    def create_documents(self, documents):
        """Bulk insert documents into the Elasticsearch index."""
        try:
            actions = [
                {
                    "_index": self.index_name,
                    "_id": doc["song_id"],
                    "_source": doc
                }
                for doc in documents
            ]
            bulk(self.es_client, actions)
            print(f"Inserted {len(actions)} documents into index '{self.index_name}'.")
        except Exception as e:
            raise RuntimeError(f"Error inserting documents: {e}")

    def search_documents(self, query:dict):
        """Search documents in the Elasticsearch index based on a query."""
        try:
            response = self.es_client.search(index=self.index_name, query=query)
            return response['hits']['hits']
        except Exception as e:
            raise RuntimeError(f"Error searching documents: {e}")

    def delete_documents(self, query:dict):
        """Delete documents in the Elasticsearch index based on a query."""
        try:
            response = self.es_client.delete_by_query(index=self.index_name, body={"query": query})
            return response
        except Exception as e:
            raise RuntimeError(f"Error deleting documents: {e}")


