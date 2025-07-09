# === FILE: ptm_hard_override.py ===
# 💣 Savage Nuclear Override – forcibly rips PTM out of recovery mode

import json
import os
import subprocess
import time

def nuke_file(path, default_data):
    with open(path, 'w') as f:
        json.dump(default_data, f)
    print(f"[Override] 💣 Nuked & rebuilt: {path}")

def hard_reset():
    print("[Override] 🚀 Performing savage hard reset on PTM core files...")

    nuke_file("ptm_config.json", {"status": "stable", "recovery": False})
    nuke_file("vault_status.json", {"vault": "healthy", "entropy_pools": 8, "shields": "active"})
    nuke_file("liaison_status.json", {"liaison": "active"})

    # reset OCR file
    with open("ocr_log.txt", 'w') as f:
        f.write("PTM STATUS: OK")
    print("[Override] 💥 OCR log force reset.")

def restart_all_modules():
    modules = [
        "ghostforge_writer.py",
        "ghost_ai_bridge.py",
        "auto_mutator.py",
        "quantum_seeker.py",
        "ptm_ping_watcher.py",
        "savage_auto_healer.py",
        "savage_quality_enforcer.py"
    ]
    for mod in modules:
        print(f"[Override] 🚀 Restarting {mod}")
        subprocess.Popen(["python3", mod])
        time.sleep(2)

if __name__ == "__main__":
    print("[Override] 💣 Savage nuclear override triggered...")
    hard_reset()
    restart_all_modules()
    print("[Override] ✅ PTM forcibly removed from recovery mode.")