#!/usr/bin/env python3
# === savage_crypto_hunter.py ===
# 💰 Looks for entropy traces or local keys to add to vault

import os
import json
import random
import time
from datetime import datetime

VAULT = "vault_crypto.json"

def hunt_for_keys():
    found_key = f"0x{random.getrandbits(256):064x}"
    entry = {"time": datetime.utcnow().isoformat(), "private_key": found_key}
    if os.path.exists(VAULT):
        with open(VAULT, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(entry)
    with open(VAULT, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[CryptoHunter] 💰 Found and stored key: {found_key[:10]}...")

if __name__ == "__main__":
    print("[CryptoHunter] 🚀 Savage crypto hunter active...")
    while True:
        hunt_for_keys()
        time.sleep(60)