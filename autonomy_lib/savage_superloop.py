# === FILE: savage_superloop.py ===
# 🧬 Savage Superloop – cycles all core systems forever

import subprocess
import time

MODULES = [
    "ghostforge_writer.py",
    "ghost_ai_bridge.py",
    "quantum_seeker.py",
    "auto_mutator.py",
    "ptm_ping_watcher.py",
    "savage_quality_enforcer.py"
]

def run_loop():
    while True:
        for mod in MODULES:
            print(f"[Superloop] 🔥 Running {mod}")
            subprocess.Popen(["python3", mod])
            time.sleep(10)
        print("[Superloop] 💤 Cycle complete. Sleeping 60s...")
        time.sleep(60)

if __name__ == "__main__":
    print("[Superloop] 🧬 Savage Superloop initialized...")
    run_loop()