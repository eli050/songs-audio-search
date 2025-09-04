from faster_whisper import WhisperModel
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from uuid import uuid4



class ReadMP3:
    def __init__(self, file_path):
        self.file_path = file_path
        self.model = WhisperModel("small", device="cpu", compute_type="int8")

    def read(self):
        audio = MP3(self.file_path, ID3=EasyID3)
        segments, info = self.model.transcribe(self.file_path, language="en")
        data_of_song = dict()
        data_of_song["song_id"] = str(uuid4())
        data_of_song["title"] = audio.get("title", ["Unknown Title"])[0]
        data_of_song["artist"] = audio.get("artist", ["Unknown Artist"])[0]
        data_of_song["lyrics"] = "\n".join([segment.text for segment in segments])
        data_of_song["link"] = self.file_path
        return data_of_song