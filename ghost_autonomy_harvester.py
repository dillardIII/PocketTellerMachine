#!/usr/bin/env python3
# 🔥 GHOST AUTONOMY HARVESTER
import os
import json

PTM_DIR = "./"  # or adjust if your clone isn't at root
HARVEST_LOG = "ghost_autonomy_harvest_log.json"
autonomy_files = []

for root, dirs, files in os.walk(PTM_DIR):
    for file in files:
        if file.endswith(".py") and ("savage" in file or "ghost" in file or "autonomy" in file):
            path = os.path.join(root, file)
            autonomy_files.append(path)

with open(HARVEST_LOG, "w") as f:
    json.dump(autonomy_files, f, indent=2)

print(f"[Harvester] ✅ Found {len(autonomy_files)} autonomy files. Log saved.")