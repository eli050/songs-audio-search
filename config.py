from elasticsearch import Elasticsearch
import streamlit as st






ES_URL = st.secrets["elasticsearch"]["url"]
ELASTICSEARCH_INDEX = st.secrets["elasticsearch"]["index"]

ES_CLIENT = Elasticsearch(
    [ES_URL],
    verify_certs=True
)


SAVE_DIR = "uploaded_songs"