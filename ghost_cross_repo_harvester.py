#!/usr/bin/env python3
# === ghost_cross_repo_harvester.py ===
# 💀 Clones PTM, finds savage autonomy files.

import os
import json
import subprocess

PTM_REPO = "https://github.com/dillardIII/PocketTellerMachine.git"
PTM_CLONE_DIR = "ptm_clone"
HARVEST_LOG = "harvest_results.json"

def clone_ptm():
    if os.path.exists(PTM_CLONE_DIR):
        subprocess.run(["rm", "-rf", PTM_CLONE_DIR])
    subprocess.run(["git", "clone", PTM_REPO, PTM_CLONE_DIR])

def find_savage_files():
    savage_files = []
    for root, dirs, files in os.walk(PTM_CLONE_DIR):
        for file in files:
            if file.endswith(".py") and ("ghost" in file or "self_" in file or "savage" in file):
                savage_files.append(os.path.join(root, file))
    return savage_files

def save_harvest(files):
    with open(HARVEST_LOG, "w") as f:
        json.dump(files, f, indent=2)
    print(f"[Harvester] ✅ Harvest results saved to {HARVEST_LOG}")

def main():
    print("[Harvester] 🔥 Cloning PTM repo...")
    clone_ptm()
    print("[Harvester] 🔍 Scanning for savage autonomy files...")
    files = find_savage_files()
    save_harvest(files)
    print(f"[Harvester] 🧬 Found {len(files)} savage files.")

if __name__ == "__main__":
    main()