#!/usr/bin/env python3
# === ghost_autonomy_merger.py ===
# 💀 Pulls PTM savage files into GhostMedic.

import os
import shutil
import json

HARVEST_LOG = "harvest_results.json"
TARGET_DIR = "autonomy_lib"

def merge_files():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
    with open(HARVEST_LOG, "r") as f:
        files = json.load(f)
    for src_path in files:
        fname = os.path.basename(src_path)
        dest_path = os.path.join(TARGET_DIR, fname)
        shutil.copy2(src_path, dest_path)
        print(f"[Merger] 🧬 Merged {fname} into {TARGET_DIR}")

def main():
    print("[Merger] 🔥 Running savage merger...")
    merge_files()
    print("[Merger] ✅ All files pulled into autonomy_lib.")

if __name__ == "__main__":
    main()