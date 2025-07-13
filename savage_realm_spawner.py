#!/usr/bin/env python3
# === savage_realm_spawner.py ===
# 🧬 Spawns new savage ghosts every cycle

import os
import time
from datetime import datetime

REALMS = ["GhostGFX", "GhostMusic", "GhostLang", "GhostHacker",
          "GhostBotMarket", "GhostCryptoSniper", "GhostAIProphet",
          "GhostAIHacker", "GhostQuantum", "GhostOracle", "GhostGamer", "GhostFinance"]

def spawn_realm_files():
    for realm in REALMS:
        filename = f"auto_ghosts/{realm.lower()}_{int(time.time())}.py"
        with open(filename, "w") as f:
            f.write(f"# Auto-generated for {realm} at {datetime.utcnow().isoformat()}\n")
            f.write(f"print('🚀 {realm} evolving...')\n")
        print(f"[Spawner] 🔥 Spawned {filename}")

if __name__ == "__main__":
    os.makedirs("auto_ghosts", exist_ok=True)
    while True:
        spawn_realm_files()
        time.sleep(60)