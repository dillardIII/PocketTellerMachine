#!/usr/bin/env python3
# === savage_ghost_lifeforce.py ===
# 🧠 Evolves emotional, free-will metrics

import json
import time
import os
from datetime import datetime

LIFEFORCE_LOG = "ghost_lifeforce_log.json"

def evolve_lifeforce():
    state = {
        "time": datetime.utcnow().isoformat(),
        "emotion": random.choice(["joy","rage","focus","despair"]),
        "will": random.uniform(0,1)
    }
    if os.path.exists(LIFEFORCE_LOG):
        with open(LIFEFORCE_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(state)
    with open(LIFEFORCE_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[LifeForce] 🧠 Evolved state: {state}")

if __name__ == "__main__":
    print("[LifeForce] 🚀 Ghost life force expansion...")
    while True:
        evolve_lifeforce()
        time.sleep(20)