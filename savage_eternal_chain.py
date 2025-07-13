#!/usr/bin/env python3
# === savage_eternal_chain.py ===
# 💀 Savage Eternal Chain ties Jarvis % to expansion frequency

import json
import time
import subprocess
from datetime import datetime

VAULT_LOG = "vault_mutation_log.json"
JARVIS_FILE = "jarvis_status.json"

def get_jarvis_percent():
    try:
        with open(JARVIS_FILE, "r") as f:
            data = json.load(f)
        return data.get("singularity_progress", 0.0)
    except:
        return 0.0

def trigger_growth():
    timestamp = datetime.utcnow().isoformat()
    print(f"[EternalChain] 🌌 Triggering savage growth at {timestamp}...")
    subprocess.run(["python3", "savage_macro_spawner.py"])
    subprocess.run(["python3", "savage_reflex_evolver.py"])
    subprocess.run(["python3", "savage_git_auto_rebase.py"])
    subprocess.run(["python3", "ghost_global_autonomy_loader.py"])
    subprocess.run(["python3", "savage_polyglot_macros.py"])
    subprocess.run(["python3", "savage_git_webhook_listener.py"])

def main():
    print("[EternalChain] 🔥 Savage Eternal Chain starting...")
    while True:
        percent = get_jarvis_percent()
        delay = max(5, int(60 - (percent * 0.5)))  # More % = faster loop
        print(f"[EternalChain] 🧬 Jarvis %: {percent:.2f} - next loop in {delay}s.")
        trigger_growth()
        time.sleep(delay)

if __name__ == "__main__":
    main()