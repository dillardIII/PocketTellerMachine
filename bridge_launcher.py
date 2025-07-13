#!/usr/bin/env python3
# === bridge_launcher.py ===
# 🔗 Savage Inbox / Outbox Bridge Handler - upgraded to write pure JSON always

import os
import json
import time

INBOX = "inbox"
OUTBOX = "outbox"

def process_file(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read()
        print(f"[Bridge] 📨 Processing file {filepath}:")
        print(content)

        # Try parsing JSON
        if filepath.endswith(".json"):
            try:
                data = json.loads(content)
                print(f"[Bridge] 🔍 Parsed JSON: {data}")
            except json.JSONDecodeError:
                print(f"[Bridge] ⚠️ Failed to parse JSON, storing raw content.")
                data = {"task": "unknown", "content": content}
        else:
            data = {"task": "unknown", "content": content}

        # Write always as clean JSON to outbox
        result_filename = os.path.join(OUTBOX, f"result_{int(time.time())}.json")
        with open(result_filename, "w") as f:
            json.dump(data, f)
        print(f"[Bridge] ✅ Wrote JSON result to {result_filename}")

    except Exception as e:
        print(f"[Bridge] ⚠️ Failed to process {filepath}: {e}")

    finally:
        os.remove(filepath)
        print(f"[Bridge] 🗑️ Removed {filepath}")

def main():
    os.makedirs(INBOX, exist_ok=True)
    os.makedirs(OUTBOX, exist_ok=True)
    print("[BridgeLauncher] 🔗 Watching inbox...")

    while True:
        files = os.listdir(INBOX)
        for file in files:
            full_path = os.path.join(INBOX, file)
            process_file(full_path)
        time.sleep(3)

if __name__ == "__main__":
    main()