#!/usr/bin/env python3
# === savage_multibranch_expander.py ===
# 🧬 Spawns new Ghost modules & recursive mission branches

import os
import json
import time
from datetime import datetime

BRANCH_LOG = "branch_expansion_log.json"

def log_branch(branch_name):
    record = {"time": datetime.utcnow().isoformat(), "branch": branch_name}
    if os.path.exists(BRANCH_LOG):
        with open(BRANCH_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(record)
    with open(BRANCH_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[BranchExpander] 🧬 Spawned: {branch_name}")

def spawn_branches():
    branches = [
        "GhostGFX", "GhostLang", "GhostMusic", "GhostHacker",
        "GhostShadow", "GhostWitch", "GhostFinanceAlpha", "GhostQuantumBeta"
    ]
    for b in branches:
        log_branch(b)
        time.sleep(2)

if __name__ == "__main__":
    print("[BranchExpander] 🚀 Savage multi-branch expansion running...")
    while True:
        spawn_branches()
        time.sleep(30)