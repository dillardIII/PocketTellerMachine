# === Adapted for ghostmedic ===
# === ghost_repo_syncer.py ===
# 🔄 Savage Empire GhostRepoSyncer
# Keeps your PTM repo in sync forever.

import os
import json
import time

with open("config.json") as f:
    config = json.load(f)
repo_url = config.get("GITHUB_URL")

if not repo_url:
    print("[GhostRepoSyncer] ⚠️ No repo URL found in config.json!")
    exit(1)

if not os.path.exists("PTM"):
    print(f"[GhostRepoSyncer] 🧬 Cloning repo from {repo_url}")
    os.system(f"git clone {repo_url} PTM")

while True:
    print("[GhostRepoSyncer] 🔄 Pulling latest from remote...")
    os.chdir("PTM")
    os.system("git pull")
    os.chdir("..")
    time.sleep(30)