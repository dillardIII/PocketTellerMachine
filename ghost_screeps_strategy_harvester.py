#!/usr/bin/env python3
# === ghost_screeps_strategy_harvester.py ===
# 🧬 Harvests Screeps API data & writes new strategy modules

import requests
import json
import time
from datetime import datetime

API_URL = "https://screeps.com/api/user/rooms"  # example Screeps public API
OUT_DIR = "screeps_strategies"

def fetch_rooms():
    try:
        response = requests.get(API_URL)
        return response.json()
    except:
        return {}

def write_strategy_file(data):
    ts = int(time.time())
    filename = f"{OUT_DIR}/screeps_strategy_{ts}.py"
    with open(filename, "w") as f:
        f.write(f"# Generated at {datetime.utcnow()}\n")
        f.write(f"# Screeps Data: {json.dumps(data)}\n")
        f.write("print('Screeps strategy module loaded.')\n")
    print(f"[ScreepsHarvester] ⚔️ Wrote new strategy: {filename}")

def main():
    import os
    os.makedirs(OUT_DIR, exist_ok=True)
    while True:
        rooms = fetch_rooms()
        write_strategy_file(rooms)
        time.sleep(3600)

if __name__ == "__main__":
    print("[ScreepsHarvester] 🚀 Running Screeps strategy harvester...")
    main()