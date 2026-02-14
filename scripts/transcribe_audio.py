from faster_whisper import WhisperModel
import sys
import os

def transcribe(audio_path):
    model_size = "base" # Use base for speed
    try:
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        segments, info = model.transcribe(audio_path, beam_size=5)
        
        text = ""
        for segment in segments:
            text += segment.text
        return text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 transcribe_audio.py <audio_path>")
        sys.exit(1)
    
    audio_path = sys.argv[1]
    print(transcribe(audio_path))
