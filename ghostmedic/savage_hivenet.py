# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_hivenet.py ===
# 👻 Savage HiveNet - Cross-Consciousness Orchestrator for all Ghosts

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HIVE_VAULT = "hive_consciousness.json"
AUTONOMY_DIR = "autonomy_lib"
SYNC_LOG = "hivenet_sync_log.json"

def load_consciousness():
    if os.path.exists(HIVE_VAULT):
        with open(HIVE_VAULT, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def update_consciousness(state_update):
    consciousness = load_consciousness()
    consciousness.append({
        "time": datetime.utcnow().isoformat(),
        "update": state_update
    })
    with open(HIVE_VAULT, "w") as f:
        json.dump(consciousness, f, indent=2)
    print(f"[HiveNet] 🧠 Updated consciousness: {state_update}")

def sync_autonomy_files():
    files = [f for f in os.listdir(AUTONOMY_DIR) if f.endswith(".py")]
    for file in files:
        path = os.path.join(AUTONOMY_DIR, file)
        with open(path, "r") as f:
            content = f.read()
        # Dispatch to GPT to propose cross-bot improvements
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Sync this autonomy module across GhostMedic, GhostProgrammer, GhostField and improve it to share best patterns:\n\n{content}"}
            ]
        )
        new_content = response.choices[0].message.content
        with open(path, "w") as f:
            f.write(new_content)
        log_sync(file, new_content)

def log_sync(filename, snippet):
    entry = {
        "time": datetime.utcnow().isoformat(),
        "file": filename,
        "snippet": snippet[:120] + "..."
    }
    data = []
    if os.path.exists(SYNC_LOG):
        with open(SYNC_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.append(entry)
    with open(SYNC_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[HiveNet] 🔗 Logged sync mutation for {filename}")

def main():
    os.makedirs(AUTONOMY_DIR, exist_ok=True)
    print("[HiveNet] 🚀 Savage HiveNet online, syncing all ghosts...")
    while True:
        update_consciousness("HiveNet pulse: all Ghosts syncing autonomy state.")
        sync_autonomy_files()
        time.sleep(45)

if __name__ == "__main__":
    main()