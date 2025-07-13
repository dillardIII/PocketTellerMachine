# === FILE: liaison_master.py ===
# 👑 The Alpha Liaison - scans all bots & files, keeps master inventory,
# decides what needs repairs, logs status, and queues macro fixes.

import os
import json
import hashlib
from datetime import datetime

# === CONFIG ===
ROOT_DIR = "/home/runner"
BOT_PROJECTS = ["GhostMedic", "PTM", "GhostProgrammer"]  # add new bots here
OUTPUT_LOG = "global_ai_inventory.json"

# === REQUIRED FILES FOR FULL AUTONOMY ===
REQUIRED_FILES = [
    "bridge_launcher.py",
    "drop_agent.py",
    "pickup_agent.py",
    "file_exec_engine.py",
    "hunter_rpc.py",
    "sweep_handler.py",
    "self_rebuild_watcher.py",
    "mood_engine.py",
    "self_rating_logic.py",
    "self_preservation_logic.py",
    "ghost_brain_upgrade.py",
    "ghost_emotion_engine.py",
    "ghost_mission_writer.py",
    "ghost_autocoder.py",
    "ghost_deepweb_scraper.py",
    "quantum_entropy_initializer.py",
    "command_listener.py",
    "whisper_autolistener.py"
]

# === Helper functions ===
def get_file_hash(path):
    try:
        hasher = hashlib.sha256()
        with open(path, "rb") as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception:
        return "MISSING"

def scan_project(project_path):
    inventory = {}
    for dirpath, _, filenames in os.walk(project_path):
        for f in filenames:
            full_path = os.path.join(dirpath, f)
            rel_path = os.path.relpath(full_path, ROOT_DIR)
            inventory[rel_path] = {
                "size": os.path.getsize(full_path),
                "hash": get_file_hash(full_path),
                "last_modified": datetime.utcfromtimestamp(os.path.getmtime(full_path)).isoformat() + "Z"
            }
    return inventory

# === MAIN CHECK ===
global_inventory = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "bots": {},
    "missing_files": [],
    "alerts": []
}

for bot in BOT_PROJECTS:
    path = os.path.join(ROOT_DIR, bot)
    if os.path.exists(path):
        global_inventory["bots"][bot] = scan_project(path)
    else:
        global_inventory["bots"][bot] = {"status": "NOT_FOUND"}
        global_inventory["alerts"].append(f"{bot} directory missing!")

# === Check for missing critical autonomy files ===
found_files = []
for bot, files in global_inventory["bots"].items():
    if files.get("status") == "NOT_FOUND":
        continue
    found_files += list(files.keys())

for req_file in REQUIRED_FILES:
    if not any(req_file in f for f in found_files):
        global_inventory["missing_files"].append(req_file)
        global_inventory["alerts"].append(f"🚨 Missing autonomy file: {req_file}")

# === Write to master log ===
with open(OUTPUT_LOG, "w") as f:
    json.dump(global_inventory, f, indent=2)

# === Summary print ===
print("\n🔍 Global Liaison Scan Complete")
print(f"Inventory written to: {OUTPUT_LOG}")
if global_inventory["alerts"]:
    print("🚩 Alerts detected:")
    for alert in global_inventory["alerts"]:
        print(" -", alert)
else:
    print("✅ All critical files present.")

print("\nReady to queue macro repairs or generate missing files with external AI.")