# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_chaos_engine.py ===
# 💥 Savage Chaos Engine - forces random mutations across autonomy

import os
import random
import json
import time
from datetime import datetime

CHAOS_LOG = "chaos_mutation_log.json"
AUTONOMY_DIR = "autonomy_lib"

def mutate_random_file():
    files = [f for f in os.listdir(AUTONOMY_DIR) if f.endswith(".py")]
    if not files:
        return None
    file = random.choice(files)
    path = os.path.join(AUTONOMY_DIR, file)
    with open(path, "a") as f:
        f.write(f"\n# ⚡ Chaos mutation at {datetime.utcnow().isoformat()}")
    return file

def log_mutation(file):
    entry = {"time": datetime.utcnow().isoformat(), "file": file}
    data = []
    if os.path.exists(CHAOS_LOG):
        with open(CHAOS_LOG, "r") as f:
            try: data = json.load(f)
            except json.JSONDecodeError: pass
    data.append(entry)
    with open(CHAOS_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Chaos] 💥 Mutated: {file}")

def main():
    print("[Chaos] 💥 Savage Chaos Engine running...")
    while True:
        mutated = mutate_random_file()
        if mutated:
            log_mutation(mutated)
        time.sleep(30)

if __name__ == "__main__":
    main()