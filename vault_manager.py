# === FILE: vault_manager.py ===
# 🔒 Manages your PTM vaults & status

import os
import time

print("[Vault Manager] 🔐 Checking vaults...")

while True:
    os.system("python3 vault_healer.py")
    os.system("python3 vaultviewer_extreme.py")
    time.sleep(30)  # adjust as needed