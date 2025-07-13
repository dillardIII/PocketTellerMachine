#!/usr/bin/env python3
# === savage_global_sync_chain.py ===
# 🌐 Savage global sync across GhostMedic, HiveNet, Reflex, etc.

import subprocess
import time
from datetime import datetime

def run_sync():
    timestamp = datetime.utcnow().isoformat()
    print(f"[GlobalSync] 🔗 Sync round at {timestamp}")
    subprocess.run(["python3", "savage_git_auto_rebase.py"])
    subprocess.run(["python3", "ghost_autonomy_jarvis_meter.py"])
    subprocess.run(["python3", "savage_macro_swarm.py"])
    subprocess.run(["python3", "hivenet_sync_manager.py"])

def main():
    print("[GlobalSync] 🌐 Starting savage global sync chain...")
    while True:
        run_sync()
        time.sleep(30)

if __name__ == "__main__":
    main()