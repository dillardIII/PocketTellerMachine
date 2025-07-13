#!/usr/bin/env python3
# 🚀 Savage Jarvis Command Listener

import json
import time
from datetime import datetime

MACRO_QUEUE = "macro_queue.json"

def append_macro(task):
    try:
        with open(MACRO_QUEUE, "r") as f:
            data = json.load(f)
    except:
        data = []

    new_macro = {"time": datetime.utcnow().isoformat(), "task": task}
    data.append(new_macro)

    with open(MACRO_QUEUE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Jarvis] 💥 Added macro: {new_macro}")

def main():
    print("[Jarvis] 🎤 Listening for your savage commands...")
    while True:
        command = input("🧬 Enter your command: ").strip()
        if command:
            append_macro(command)
        time.sleep(1)

if __name__ == "__main__":
    main()