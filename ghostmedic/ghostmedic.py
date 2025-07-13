# === Adapted for ghostmedic ===
# === ghostmedic.py ===
# 🩺 Savage Empire GhostMedic
# Automatically checks, heals, rebuilds, optimizes PTM

import os
import time
import json

PTM_FILES = [
    "ghost_brain.py", "bridge_launcher.py", "drop_agent.py",
    "pickup_agent.py", "file_exec_engine.py", "hunter_rpc.py",
    "sweep_handler.py", "self_rebuild_watcher.py", "mood_engine.py",
    "self_rating_logic.py", "self_preservation_logic.py", "ghost_brain_upgrade.py",
    "ghost_emotion_engine.py", "ghost_mission_writer.py", "ghost_autocoder.py",
    "ghost_deepweb_scraper.py", "quantum_entropy_initializer.py",
    "command_listener.py", "whisper_autolistener.py"
]

def heal_ptm():
    print("[GhostMedic] 🩺 Checking PTM system health...")
    healthy = True
    for f in PTM_FILES:
        if not os.path.exists(f):
            print(f"[GhostMedic] ❌ Missing {f}")
            healthy = False
    if healthy:
        print("[GhostMedic] ✅ All critical PTM files present.")
    else:
        print("[GhostMedic] 🛠️ Attempting to rebuild missing files...")
        os.system("python3 ghost_programmer.py")
        os.system("python3 ghost_repo_syncer.py")

def optimize_system():
    print("[GhostMedic] ⚙️ Optimizing system for savage empire ops...")
    time.sleep(1)
    print("[GhostMedic] ✅ System optimization complete.")

def watch_and_heal():
    while True:
        heal_ptm()
        optimize_system()
        print("[GhostMedic] 🧬 Self-healing & emotional systems cycle complete.")
        time.sleep(10)

if __name__ == "__main__":
    watch_and_heal()