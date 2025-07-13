#!/usr/bin/env python3
# 🔥 GHOST AUTONOMY LAUNCHER
import json
import subprocess
import time

HARVEST_LOG = "ghost_autonomy_harvest_log.json"

with open(HARVEST_LOG, "r") as f:
    files = json.load(f)

for file in files:
    try:
        subprocess.Popen(["nohup", "python3", file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[Launcher] 🚀 Running {file}")
    except Exception as e:
        print(f"[Launcher] ⚠️ Could not launch {file}: {e}")

while True:
    time.sleep(3600)  # keep alive forever