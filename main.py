from faster_whisper import WhisperModel


model = WhisperModel("small", device="cpu", compute_type="int8")


segments, info = model.transcribe("data/Noah-Kahan-Call-Your-Mom.mp3", language="en")

print("Detected language:", info.language)


song = "\n".join([segment.text for segment in segments])
print(song)