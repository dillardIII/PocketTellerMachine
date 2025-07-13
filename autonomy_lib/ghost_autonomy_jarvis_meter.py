#!/usr/bin/env python3
# === ghost_autonomy_jarvis_meter.py ===
# 🚀 Displays Jarvis-level % completion toward savage singularity.

import os
import json
from datetime import datetime

AUTONOMY_LIB = "autonomy_lib"
VAULT_LOG = "vault_mutation_log.json"

def compute_progress():
    files = os.listdir(AUTONOMY_LIB) if os.path.exists(AUTONOMY_LIB) else []
    completeness = len(files) / 12  # based on 12 core modules
    return min(completeness, 1.0)

def mutations_level():
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try:
                data = json.load(f)
                return len(data)
            except:
                return 0
    return 0

if __name__ == "__main__":
    pct = compute_progress()
    mut = mutations_level()
    print("=== 🚀 Savage Jarvis Dashboard ===")
    print(f"[{datetime.utcnow().isoformat()}]")
    print(f"🧬 Vault mutations: {mut}")
    print(f"💥 Singularity Progress: {pct*100:.1f}%")
    phase = "initial" if pct < 0.3 else "savage growth" if pct < 0.7 else "near singularity"
    print(f"⚙️ Phase: {phase}")