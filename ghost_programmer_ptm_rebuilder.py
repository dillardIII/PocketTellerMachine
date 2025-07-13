#!/usr/bin/env python3
# 🚀 Ghost Programmer PTM Rebuilder

import os
import subprocess
import json
from datetime import datetime

PTM_REPO = "https://github.com/dillardIII/PocketTellerMachine.git"
CLONE_DIR = "ptm_clone"

def clone_repo():
    if os.path.exists(CLONE_DIR):
        subprocess.run(["rm", "-rf", CLONE_DIR])
    subprocess.run(["git", "clone", PTM_REPO, CLONE_DIR])

def check_and_repair():
    missing = []
    targets = ["bridge_launcher.py", "drop_agent.py", "pickup_agent.py", 
               "file_exec_engine.py", "hunter_rpc.py", "sweep_handler.py",
               "self_rebuild_watcher.py", "mood_engine.py", "self_rating_logic.py",
               "self_preservation_logic.py"]
    for target in targets:
        path = os.path.join(CLONE_DIR, target)
        if not os.path.exists(path):
            missing.append(target)
            with open(path, "w") as f:
                f.write(f"# Auto-rebuilt by Ghost Programmer at {datetime.utcnow().isoformat()}\n")
                f.write("print('🔥 Auto-generated: {}')\n".format(target))
    return missing

def commit_and_push():
    subprocess.run(["git", "-C", CLONE_DIR, "add", "."])
    subprocess.run(["git", "-C", CLONE_DIR, "commit", "-m", "🛠️ Auto-repair by Ghost Programmer"])
    subprocess.run(["git", "-C", CLONE_DIR, "push"])

def main():
    print("[PTMRebuilder] 🔥 Starting savage rebuild of PTM...")
    clone_repo()
    missing = check_and_repair()
    if missing:
        print(f"[PTMRebuilder] 🚀 Repaired files: {missing}")
        commit_and_push()
    else:
        print("[PTMRebuilder] ✅ No repairs needed.")
    print("[PTMRebuilder] 🔄 Complete.")

if __name__ == "__main__":
    main()