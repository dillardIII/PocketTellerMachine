#!/usr/bin/env python3
# === savage_jarvis_loop_eternal.py ===
# 🚀 Eternal Jarvis Loop - pushes your savage empire to full singularity

import os
import json
import time
from datetime import datetime
from subprocess import run

VAULT_LOG = "vault_mutation_log.json"
MACRO_QUEUE = "macro_queue.json"

def calc_jarvis_percentage():
    mutations = 0
    macros = 0
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try:
                data = json.load(f)
                mutations = len(data)
            except json.JSONDecodeError:
                pass
    if os.path.exists(MACRO_QUEUE):
        with open(MACRO_QUEUE, "r") as f:
            try:
                data = json.load(f)
                macros = len(data)
            except json.JSONDecodeError:
                pass
    jarvis_level = min((mutations + macros) / 1000, 1.0) * 100
    return round(jarvis_level, 2)

def spawn_more_savage_files(jarvis_percent):
    if jarvis_percent < 20:
        freq = 60
    elif jarvis_percent < 50:
        freq = 30
    elif jarvis_percent < 80:
        freq = 15
    else:
        freq = 5
    print(f"[JarvisLoop] 💥 Spawning savage mutations every {freq}s.")
    time.sleep(freq)
    # simulate mutation
    run(["python3", "savage_macro_spawner.py"])
    run(["python3", "savage_quantum_chaos_engine.py"])

def auto_git_push():
    print("[JarvisLoop] 🔗 Auto pushing to Git...")
    run(["python3", "savage_git_auto_rebase.py"])

def main():
    while True:
        jarvis_percent = calc_jarvis_percentage()
        print(f"[JarvisLoop] 🚀 JARVIS LEVEL: {jarvis_percent}% towards singularity.")
        if jarvis_percent >= 100:
            print("[JarvisLoop] 💀 FULL SINGULARITY ACHIEVED! Locking eternal expansion.")
        spawn_more_savage_files(jarvis_percent)
        auto_git_push()

if __name__ == "__main__":
    main()