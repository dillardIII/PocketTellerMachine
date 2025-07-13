#!/usr/bin/env python3
# === savage_macro_spawner.py ===
# 🐉 Feeds your macro swarm with new evolving tasks forever

import json
import time
import os
from datetime import datetime
import random

MACRO_QUEUE = "macro_queue.json"

def load_macros():
    if os.path.exists(MACRO_QUEUE):
        with open(MACRO_QUEUE, "r") as f:
            return json.load(f)
    return []

def save_macros(macros):
    with open(MACRO_QUEUE, "w") as f:
        json.dump(macros, f, indent=2)

def generate_macro():
    tasks = [
        "rebuild ghostmedic.py",
        "optimize savage_macro_dashboard.py",
        "patch vault system",
        "auto-create savage swarm agent",
        "mutate savage quantum reflex",
        "evolve new trade logic",
        "reinforce ghost emotional shields",
        "deploy scout bots to shadow net"
    ]
    return {
        "time": datetime.utcnow().isoformat(),
        "task": random.choice(tasks),
        "priority": random.randint(50,100)
    }

def main():
    print("[MacroSpawner] 🧬 Savage macro spawner active...")
    while True:
        macros = load_macros()
        new_macro = generate_macro()
        macros.append(new_macro)
        save_macros(macros)
        print(f"[MacroSpawner] 🔥 Added macro: {new_macro}")
        time.sleep(10)

if __name__ == "__main__":
    main()