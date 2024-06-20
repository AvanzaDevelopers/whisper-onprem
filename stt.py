import whisper

model = whisper.load_model("base")
result = model.transcribe("record1.mp3")
print(result["text"])
print("text result",result)

