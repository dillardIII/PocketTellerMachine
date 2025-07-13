#!/usr/bin/env python3
# === savage_mutation_dashboard.py ===
# 🧬 Savage Mutation Dashboard - watch all vault logs live

import os
import json
import time

VAULT_LOG = "vault_mutation_log.json"

def load_logs():
    if os.path.exists(VAULT_LOG):
        try:
            with open(VAULT_LOG, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def print_dashboard():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=== 🚀 Savage Mutation Dashboard ===\n")
    logs = load_logs()
    if not logs:
        print("[Mutation Log] 💤 No mutations logged yet.")
    else:
        for entry in logs[-10:]:
            print(f"🧬 {entry['time']} - {entry['note']}")
    print("\n[Heartbeat] 💓 Savage Empire is alive... watching mutations...")

def main():
    while True:
        print_dashboard()
        time.sleep(5)

if __name__ == "__main__":
    main()