#!/usr/bin/env python3
# === savage_vault_extender.py ===
# 🔒 Keeps growing the vault to accept all kinds of data

import os
import json
import time
from datetime import datetime

VAULT = "vault_master.json"

def extend_vault(new_data):
    if os.path.exists(VAULT):
        with open(VAULT, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append({"time": datetime.utcnow().isoformat(), "data": new_data})
    with open(VAULT, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[VaultExtender] 🔒 Vault extended with: {new_data}")

if __name__ == "__main__":
    print("[VaultExtender] 🚀 Running continuous vault extension...")
    while True:
        extend_vault("auto-entropy-seed-" + datetime.utcnow().isoformat())
        time.sleep(20)