#!/usr/bin/env python3
# === ghost_ptm_harvester.py ===
# 🧬 Harvests PTM autonomy files for Ghost Empire use.

import os
import shutil
import subprocess

PTM_REPO = "https://github.com/dillardIII/PocketTellerMachine.git"
CLONE_DIR = "ptm_clone"
AUTONOMY_LIB = "autonomy_lib"
FILES_TO_HARVEST = [
    "bridge_launcher.py",
    "ghost_brain.py",
    "drop_agent.py",
    "pickup_agent.py",
    "file_exec_engine.py",
    "hunter_rpc.py",
    "sweep_handler.py",
    "self_rebuild_watcher.py",
    "mood_engine.py",
    "self_rating_logic.py",
    "self_preservation_logic.py"
]

def clone_repo():
    if os.path.exists(CLONE_DIR):
        shutil.rmtree(CLONE_DIR)
    print("[Harvester] 🔥 Cloning PTM repo...")
    subprocess.run(["git", "clone", PTM_REPO, CLONE_DIR])

def extract_files():
    os.makedirs(AUTONOMY_LIB, exist_ok=True)
    for f in FILES_TO_HARVEST:
        src_path = os.path.join(CLONE_DIR, f)
        dest_path = os.path.join(AUTONOMY_LIB, f)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"[Harvester] ✅ Copied {f} to autonomy_lib.")
        else:
            print(f"[Harvester] ⚠️ {f} not found in PTM repo.")

if __name__ == "__main__":
    clone_repo()
    extract_files()
    print("[Harvester] 🌱 Autonomy library is ready.")