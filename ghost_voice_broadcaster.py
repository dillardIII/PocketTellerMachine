#!/usr/bin/env python3
# 🚀 Ghost Voice Broadcaster - savage empire speaks

import os
import json
import time
import pyttsx3

VAULT_LOG = "vault_mutation_log.json"
MACRO_QUEUE = "macro_queue.json"

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"[Voice] 🎤 {text}")
    engine.say(text)
    engine.runAndWait()

def read_json_file(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return []

def main():
    last_vault_count = 0
    last_macro_count = 0

    while True:
        vault_data = read_json_file(VAULT_LOG)
        macro_data = read_json_file(MACRO_QUEUE)

        if len(vault_data) > last_vault_count:
            new_entries = vault_data[last_vault_count:]
            for entry in new_entries:
                speak(f"Vault log: {entry.get('task', '')}")
            last_vault_count = len(vault_data)

        if len(macro_data) > last_macro_count:
            new_entries = macro_data[last_macro_count:]
            for entry in new_entries:
                speak(f"Macro: {entry.get('task', '')}")
            last_macro_count = len(macro_data)

        time.sleep(5)

if __name__ == "__main__":
    speak("Savage Ghost Voice online. Awaiting new logs.")
    main()