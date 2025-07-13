#!/usr/bin/env python3
# === repo_inspector.py ===
# 🔍 Savage Repo Inspector - checks PTM file health and builds macro queue

import os
import json
import time

TARGET_DIR = "./PTM"  # or your direct workspace root
MACRO_QUEUE = "macro_queue.json"

CRITICAL_FILES = [
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

def inspect_repo():
    missing = []
    for file in CRITICAL_FILES:
        full_path = os.path.join(TARGET_DIR, file)
        if not os.path.exists(full_path):
            missing.append({
                "action": "generate_or_repair_file",
                "details": f"autobuild missing {file}"
            })
    return missing

def update_macro_queue(missing_tasks):
    if os.path.exists(MACRO_QUEUE):
        with open(MACRO_QUEUE, "r") as f:
            try:
                queue = json.load(f)
            except json.JSONDecodeError:
                queue = []
    else:
        queue = []

    queue.extend(missing_tasks)

    with open(MACRO_QUEUE, "w") as f:
        json.dump(queue, f, indent=2)

    print(f"[RepoInspector] 📜 Added {len(missing_tasks)} tasks to macro queue.")

def main():
    print("[RepoInspector] 🔍 Scanning repo for missing savage files...")
    missing_tasks = inspect_repo()
    if missing_tasks:
        update_macro_queue(missing_tasks)
    else:
        print("[RepoInspector] ✅ All critical files present. No tasks added.")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(30)  # scan every 30s, you can tune it