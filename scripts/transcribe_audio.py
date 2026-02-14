from faster_whisper import WhisperModel
import sys
import os

def transcribe(audio_path):
    model_size = "small" # Upgraded from base to small for better Hindi/multilingual accuracy
    try:
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        # Added initial_prompt to guide the model towards Hindi/English
        segments, info = model.transcribe(audio_path, beam_size=5, initial_prompt="Hindi, English, Hinglish audio transcript.")
        
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
