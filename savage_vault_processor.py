#!/usr/bin/env python3
# === savage_vault_processor.py ===
# 🚀 Savage Vault Processor - scans vault_docs and logs findings

import os
import json
import time
from datetime import datetime

VAULT_DIR = "vault_docs"
VAULT_LOG = "vault_mutation_log.json"

def log_vault_entry(note):
    entry = {"time": datetime.utcnow().isoformat(), "note": note}
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(entry)
    with open(VAULT_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[VaultProc] 🔏 Logged: {note}")

def process_files():
    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR)
        print(f"[VaultProc] 📂 Created missing vault dir: {VAULT_DIR}")

    for fname in os.listdir(VAULT_DIR):
        fpath = os.path.join(VAULT_DIR, fname)
        if os.path.isfile(fpath):
            with open(fpath, "r", errors="ignore") as f:
                content = f.read(200)  # preview
            log_vault_entry(f"Processed {fname}: starts with '{content[:50]}'")
            os.remove(fpath)
            print(f"[VaultProc] 🗑️ Removed {fname} after processing.")

def main():
    print("[VaultProc] 🚀 Savage vault processor running...")
    while True:
        process_files()
        print("[VaultProc] ⏳ Waiting 30s...")
        time.sleep(30)

if __name__ == "__main__":
    main()
