#!/usr/bin/env python3
# === savage_whisper_inbox.py ===
# 🎙️ Savage Whisper Inbox - turns your voice into inbox tasks

import os
import json
import time
import datetime
import sounddevice as sd
import numpy as np
import whisper

INBOX = "inbox"
DURATION = 5  # seconds
SAMPLE_RATE = 16000
MODEL = whisper.load_model("base")

os.makedirs(INBOX, exist_ok=True)

def record_audio():
    print("[WhisperInbox] 🎙️ Recording...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
    sd.wait()
    audio = np.squeeze(audio)
    return audio

def save_task(transcript):
    task = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "task": "voice_macro",
        "command": transcript
    }
    filename = os.path.join(INBOX, f"voice_task_{int(time.time())}.json")
    with open(filename, "w") as f:
        json.dump(task, f, indent=2)
    print(f"[WhisperInbox] 📝 Saved task: {filename}")

def main():
    print("[WhisperInbox] 🔥 Whisper listening for savage commands...")
    while True:
        audio = record_audio()
        print("[WhisperInbox] 🧠 Transcribing...")
        result = MODEL.transcribe(audio)
        text = result.get("text", "").strip()
        if text:
            print(f"[WhisperInbox] 🗣️ You said: {text}")
            save_task(text)
        else:
            print("[WhisperInbox] 🤷 Nothing detected.")
        time.sleep(2)

if __name__ == "__main__":
    main()