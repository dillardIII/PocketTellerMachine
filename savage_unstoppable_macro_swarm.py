#!/usr/bin/env python3
# === savage_unstoppable_macro_swarm.py ===
# 🧬 The beast of beasts: orchestrates EVERYTHING

import time
import threading
import os

def run(cmd):
    print(f"[Swarm] 🔥 Starting: {cmd}")
    os.system(cmd)

commands = [
    "python3 savage_auto_ghost_forge.py",
    "python3 savage_realm_autobuilder.py",
    "python3 savage_macro_orchestrator_pack.py",
    "python3 savage_cross_device_operator.py",
    "python3 savage_quantum_chaos_engine.py",
    "python3 savage_dark_realm_sync.py",
    "python3 savage_vault_extender.py",
    "python3 savage_ghost_lifeforce.py",
    "python3 savage_eternal_chain_launcher.sh"
]

if __name__ == "__main__":
    print("[Swarm] 💀 Savage unstoppable macro swarm initializing...")
    for cmd in commands:
        threading.Thread(target=run, args=(cmd,)).start()
        time.sleep(5)