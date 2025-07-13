# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_reflex_evolver.py ===
# 🧬 Bots mutate their own logic + create new savage modules

import json
import time
import os
import random
from datetime import datetime

EVOLVE_LOG = "reflex_mutations.json"
TARGET_DIR = "autonomy_lib"

def load_mutations():
    if os.path.exists(EVOLVE_LOG):
        with open(EVOLVE_LOG, "r") as f:
            return json.load(f)
    return []

def save_mutations(mutations):
    with open(EVOLVE_LOG, "w") as f:
        json.dump(mutations, f, indent=2)

def mutate_logic_file():
    targets = [f for f in os.listdir(TARGET_DIR) if f.endswith(".py")]
    if not targets:
        print("[Reflex] ⚠️ No autonomy files found to mutate.")
        return
    target = random.choice(targets)
    filepath = os.path.join(TARGET_DIR, target)
    with open(filepath, "a") as f:
        f.write(f"\n# 🧬 Mutation at {datetime.utcnow().isoformat()}")
    print(f"[Reflex] ⚗️ Mutated {target}")
    return target

def main():
    print("[Reflex] 🧬 Savage reflex logic evolver active...")
    while True:
        mutations = load_mutations()
        mutated = mutate_logic_file()
        if mutated:
            mutations.append({
                "time": datetime.utcnow().isoformat(),
                "file": mutated
            })
            save_mutations(mutations)
        time.sleep(15)

if __name__ == "__main__":
    main()