#!/usr/bin/env python3
"""
FULL AUTONOMY LAUNCHER
- Launches your entire savage empire stack
- Includes PTM ping watcher to keep PTM out of recovery mode
- Unreal, Render, Tasker, Quantum, PEWAC, GhostForge, and more
"""

import subprocess
import time

COMMANDS = [
    "python3 auto_mutator.py",
    "python3 ghostforge_writer.py",
    "python3 pewac_ops.py",
    "python3 quantum_seeker.py",
    "python3 unreal_bridge.py",
    "python3 render_sync.py",
    "python3 tasker_webhook_trigger.py",
    "python3 ptm_ping_watcher.py"
]

def launch_empire():
    procs = []
    for cmd in COMMANDS:
        print(f"🚀 Launching: {cmd}")
        procs.append(subprocess.Popen(cmd, shell=True))
    return procs

if __name__ == "__main__":
    procs = launch_empire()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("🛑 Shutting down savage empire...")
        for p in procs:
            p.kill()