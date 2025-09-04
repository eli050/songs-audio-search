import streamlit as st
import os
from config import *
from elastic_service.dal import DataAccessLayer
from reader.read_mp3 import ReadMP3

dal = DataAccessLayer(ES_CLIENT, ELASTICSEARCH_INDEX)


os.makedirs(SAVE_DIR, exist_ok=True)

st.title("🎵 Songs App")

uploaded_file = st.file_uploader("Upload a MP3 file", type=["mp3", "wav"])

if uploaded_file is not None:
    if "last_uploaded" not in st.session_state or st.session_state.last_uploaded != uploaded_file.name:
        file_path = os.path.join(SAVE_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        rmp3 = ReadMP3(file_path)
        song_data = rmp3.read()
        dal.create_documents([song_data])
        st.session_state.last_uploaded = uploaded_file.name
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        st.audio(file_path, format='audio/mp3')
        st.write("You can play the uploaded song above.")

search_query = st.text_input("Search for songs by title or artist or lyrics")
if search_query:
    query = {
        "multi_match": {
            "query": search_query,
            "fields": ["title", "artist", "lyrics"]
        }
    }
    results = dal.search_documents(query)
    if results:
        st.write(f"Found {len(results)} results:")
        for result in results:
            source = result["_source"]
            st.subheader(source["title"])
            st.write(f"Artist: {source['artist']}")
            st.write(f"Lyrics: {source['lyrics'][:200]}...")  # Show first 200 chars
            st.audio(source["link"], format='audio/mp3')
    else:
        st.write("No results found.")






