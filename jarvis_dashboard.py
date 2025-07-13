#!/usr/bin/env python3
# === jarvis_dashboard.py ===
# 🤖 Savage Jarvis Level Meter - shows % progress to singularity based on vault log

import json
import time
import os
from datetime import datetime

VAULT_LOG = "vault_mutation_log.json"

def calc_progress(entries):
    """
    Calculates % progress to singularity.
    This is intentionally savage: each new vault entry pushes closer to the threshold.
    """
    total_steps_required = 1000  # arbitrary savage singularity goal
    progress = min(len(entries) / total_steps_required * 100, 100)
    return round(progress, 2)

def display_dashboard(entries):
    os.system('clear' if os.name == 'posix' else 'cls')
    progress = calc_progress(entries)
    print("=== 🚀 Savage Jarvis Dashboard ===")
    print(f"[{datetime.utcnow().isoformat()}]")
    print(f"🧬 Vault mutations: {len(entries)}")
    print(f"💥 Singularity Progress: {progress}%")
    if progress < 30:
        print("⚙️ Early savage evolution phase.")
    elif progress < 70:
        print("🔥 Mid-level empire construction.")
    else:
        print("🚀 Approaching full savage singularity...")

def load_vault_log():
    if not os.path.exists(VAULT_LOG):
        return []
    with open(VAULT_LOG, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def main():
    while True:
        entries = load_vault_log()
        display_dashboard(entries)
        time.sleep(5)

if __name__ == "__main__":
    main()