# === FILE: savage_auto_healer.py ===
# 🩹 Savage Auto-Healer – scans for issues & restarts broken modules

import os
import json
import subprocess
import time

def check_json_file(filepath):
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return True
    except Exception:
        return False

def restart_ptm_modules():
    print("[Auto-Healer] 🔥 Restarting core savage modules...")
    modules = [
        "ghostforge_writer.py",
        "ghost_ai_bridge.py",
        "quantum_seeker.py",
        "auto_mutator.py",
        "ptm_ping_watcher.py"
    ]
    for mod in modules:
        print(f"[Auto-Healer] 🚀 Running {mod}...")
        subprocess.Popen(["python3", mod])
    print("[Auto-Healer] ✅ Restarted all modules.")

def heal_loop():
    while True:
        issues_found = False

        for file in ["ptm_config.json", "vault_status.json", "liaison_status.json"]:
            if not check_json_file(file):
                print(f"[Auto-Healer] ⚠️ Found corrupted or missing: {file}")
                with open(file, 'w') as f:
                    json.dump({"reset": True}, f)
                issues_found = True

        if issues_found:
            restart_ptm_modules()

        time.sleep(60)

if __name__ == "__main__":
    print("[Auto-Healer] 🩹 Savage Auto-Healer started...")
    heal_loop()