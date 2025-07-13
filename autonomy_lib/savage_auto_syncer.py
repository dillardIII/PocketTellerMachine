#!/usr/bin/env python3
# === savage_auto_syncer.py ===
# 🌐 Savage Auto-Syncer - wires all bridges, inbox/outbox, across all future bots

import os
import json
import time
from datetime import datetime

# Known global resources
SYNC_FILES = [
    "quantum_shards.json",
    "sync_mesh.json",
    "macro_queue.json",
    "vault_status.json"
]

SYNC_DIRS = [
    "inbox",
    "outbox"
]

SYNC_STATE_FILE = "global_sync_state.json"

def load_json_safe(filepath, default):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return default

def sync_json_file(filename):
    """ Ensure a global sync file exists, if not create basic structure """
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump([], f) if filename.endswith(".json") else f.write("")
        print(f"[AutoSync] 🔧 Created missing {filename}")

def sync_directory(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print(f"[AutoSync] 📁 Created missing directory: {dirname}")

def update_global_sync_state():
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "files": {},
        "dirs": {}
    }
    for f in SYNC_FILES:
        if os.path.exists(f):
            state["files"][f] = os.path.getsize(f)
    for d in SYNC_DIRS:
        if os.path.exists(d):
            state["dirs"][d] = len(os.listdir(d))
    with open(SYNC_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
    print(f"[AutoSync] 🧬 Updated global sync state.")

def main():
    print("[AutoSync] 🌐 Starting Savage Auto-Syncer...")
    while True:
        # ensure all files and dirs exist
        for f in SYNC_FILES:
            sync_json_file(f)
        for d in SYNC_DIRS:
            sync_directory(d)

        # save global state snapshot
        update_global_sync_state()
        time.sleep(5)

if __name__ == "__main__":
    main()