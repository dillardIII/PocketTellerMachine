#!/usr/bin/env python3
# === savage_quantum_jarvis_chain.py ===
import os, json, random, time
from datetime import datetime

JARVIS_FILE = "jarvis_status.json"
MACRO_QUEUE = "macro_queue.json"
VAULT_LOG = "vault_mutation_log.json"
AUTONOMY_DIR = "autonomy_lib/"

def load_jarvis_percent():
    if os.path.exists(JARVIS_FILE):
        with open(JARVIS_FILE) as f:
            data = json.load(f)
            return data.get("jarvis_percent", 0)
    return 0

def evolve_files():
    files = [f for f in os.listdir(AUTONOMY_DIR) if f.endswith(".py")]
    random.shuffle(files)
    for f in files[:random.randint(1, 3)]:
        path = os.path.join(AUTONOMY_DIR, f)
        with open(path, "a") as file:
            file.write(f"\n# 🔥 Auto-mutated at {datetime.utcnow().isoformat()} with quantum pulse.")
    print(f"[QuantumJarvis] 🧬 Mutated {len(files[:3])} files.")

def queue_macro():
    task = {"time": datetime.utcnow().isoformat(), "task": "quantum jarvis expansion"}
    if os.path.exists(MACRO_QUEUE):
        with open(MACRO_QUEUE) as f:
            macros = json.load(f)
    else:
        macros = []
    macros.append(task)
    with open(MACRO_QUEUE, "w") as f:
        json.dump(macros, f, indent=2)

def log_vault():
    entry = {"time": datetime.utcnow().isoformat(), "event": "jarvis quantum evolution"}
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG) as f:
            log = json.load(f)
    else:
        log = []
    log.append(entry)
    with open(VAULT_LOG, "w") as f:
        json.dump(log, f, indent=2)

while True:
    percent = load_jarvis_percent()
    cycles = max(1, int(percent // 10))
    print(f"[QuantumJarvis] 🚀 Running {cycles} savage evolution cycles (Jarvis %: {percent})")
    for _ in range(cycles):
        evolve_files()
        queue_macro()
        log_vault()
    time.sleep(60)