import whisperx

def transcribeAudio(audio_path):
    try:
        print("Transcribing audio...")

        whisperx.load_model("large-v2", "cuda", compute_type="float16")
        audio = whisperx.load_audio(audio_path)
        segments, info = model.transcribe(audio, batch_size=16)
        print("Model loaded")
        segments = list(segments)
        # print(segments)
        extracted_texts = [[segment.text, segment.start, segment.end] for segment in segments]
        return extracted_texts
    except Exception as e:
        print("Transcription Error:", e)
        return []

if __name__ == "__main__":
    audio_path = "audio.wav"
    transcriptions = transcribeAudio(audio_path)
    print("Done")
    TransText = ""

    for text, start, end in transcriptions:
        TransText += (f"{start} - {end}: {text}")
    print(TransText)