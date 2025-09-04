import os
from elasticsearch import Elasticsearch



ELASTICSEARCH_WWW = os.getenv('ELASTICSEARCH_WWW', 'http')
ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'localhost')
ELASTICSEARCH_PORT = int(os.getenv('ELASTICSEARCH_PORT', 9200))
ELASTICSEARCH_INDEX = os.getenv('ELASTICSEARCH_INDEX', 'songs_index')


ES_CLIENT = Elasticsearch(ELASTICSEARCH_WWW + "://" + ELASTICSEARCH_HOST + ":" + str(ELASTICSEARCH_PORT))



SAVE_DIR = os.getenv('SAVE_DIR', "uploaded_songs")