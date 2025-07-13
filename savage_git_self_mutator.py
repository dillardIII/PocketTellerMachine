#!/usr/bin/env python3
# === savage_git_self_mutator.py ===
# 🧬 The savage script that rewrites savage_git_auto_rebase.py over time

import json
import time
from datetime import datetime

TARGET = "savage_git_auto_rebase.py"

def mutate_script():
    with open(TARGET, "r") as f:
        lines = f.readlines()
    mutation = f"# 🧬 Mutation at {datetime.utcnow().isoformat()}\n"
    lines.insert(-1, mutation)
    with open(TARGET, "w") as f:
        f.writelines(lines)
    print(f"[SelfMutator] ⚗️ Mutated {TARGET}")

def main():
    print("[SelfMutator] 🔥 Savage git self-mutator running...")
    while True:
        mutate_script()
        time.sleep(60)

if __name__ == "__main__":
    main()