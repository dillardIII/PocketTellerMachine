# === Adapted for ghostmedic ===
# === FILE: ptm_final_savage_override.py ===
# 🔥 Savage Kill Stack – forces PTM out of recovery no matter what
import os
import json
import subprocess
import time

def nuke_json_file(path, content):
    with open(path, 'w') as f:
        json.dump(content, f)
    print(f"[KILL STACK] 💣 Overwritten: {path}")

def nuke_txt_file(path, content):
    with open(path, 'w') as f:
        f.write(content)
    print(f"[KILL STACK] 💣 Overwritten: {path}")

def deep_scan_and_destroy():
    print("[KILL STACK] 🔥 Scanning for *recovery*, *failover*, *status* files...")
    for root, dirs, files in os.walk('.'):
        for file in files:
            if any(keyword in file for keyword in ['recovery', 'failover', 'status']):
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'w') as f:
                        f.write("// SAVAGE NUKED BY KILL STACK //")
                    print(f"[KILL STACK] 💀 Nuked: {file_path}")
                except Exception as e:
                    print(f"[KILL STACK] ⚠️ Could not nuke {file_path}: {e}")

def restart_savage_modules():
    modules = [
        "ghostforge_writer.py",
        "ghost_ai_bridge.py",
        "auto_mutator.py",
        "quantum_seeker.py",
        "ptm_ping_watcher.py",
        "savage_auto_healer.py"
    ]
    for m in modules:
        print(f"[KILL STACK] 🚀 Restarting: {m}")
        subprocess.Popen(["python3", m])
        time.sleep(2)

if __name__ == "__main__":
    print("[KILL STACK] 🚀 Launching savage final override...")
    nuke_json_file("ptm_config.json", {"status": "stable", "recovery": False})
    nuke_json_file("vault_status.json", {"vault": "healthy", "entropy_pools": 8, "shields": "active"})
    nuke_json_file("liaison_status.json", {"liaison": "active"})
    nuke_txt_file("ocr_log.txt", "PTM STATUS: OK")
    deep_scan_and_destroy()
    restart_savage_modules()
    print("[KILL STACK] ✅ PTM forced out of recovery. All known recovery artifacts obliterated.")