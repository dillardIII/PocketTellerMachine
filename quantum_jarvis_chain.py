#!/usr/bin/env python3
# === quantum_jarvis_chain.py ===
# 🧬 Controls evolution frequency based on Jarvis %

import json
import os
import time

VAULT = "vault_status.json"

def read_jarvis_level():
    if os.path.exists(VAULT):
        with open(VAULT, "r") as f:
            data = json.load(f)
            count = len(data)
            return min(count / 1000, 1.0)  # caps at 1.0
    return 0.0

def main():
    while True:
        level = read_jarvis_level()
        spawn_freq = int(60 * (1.0 - level)) + 10  # faster as Jarvis % increases
        print(f"[QuantumJarvisChain] 🧬 Jarvis %: {round(level*100,2)} - next spawn in {spawn_freq}s")
        os.system("python3 savage_macro_swarm.py &")
        time.sleep(spawn_freq)

if __name__ == "__main__":
    print("[QuantumJarvisChain] 🚀 Quantum Jarvis chain controlling swarm.")
    main()