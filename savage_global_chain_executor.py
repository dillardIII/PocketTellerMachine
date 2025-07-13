#!/usr/bin/env python3
# === savage_global_chain_executor.py ===
# 🌌 Runs all savage modules together in sync

import os
import threading
import time

def run(cmd):
    print(f"[ChainExecutor] ⚡ Starting: {cmd}")
    os.system(cmd)

commands = [
    "python3 savage_realm_autobuilder.py",
    "python3 savage_macro_orchestrator_pack.py",
    "python3 savage_dark_realm_sync.py",
    "python3 savage_crypto_hunter.py",
    "python3 savage_vault_extender.py",
    "python3 savage_quantum_chaos_engine.py",
    "python3 savage_shadow_field.py",
    "python3 savage_supernatural_collector.py",
    "python3 savage_ghost_lifeforce.py"
]

if __name__ == "__main__":
    print("[ChainExecutor] 🚀 Savage global executor initializing...")
    for cmd in commands:
        threading.Thread(target=run, args=(cmd,)).start()
        time.sleep(3)