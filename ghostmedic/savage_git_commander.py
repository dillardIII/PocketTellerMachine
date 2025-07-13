# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_git_commander.py ===
# 👾 Savage Git Commander - autonomous git commit & push

import subprocess
import time
from datetime import datetime

GIT_LOG = "git_autonomy_log.txt"

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr

def log(msg):
    with open(GIT_LOG, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} - {msg}\n")
    print(msg)

def main():
    print("[GitCommander] 🚀 Savage Git Commander starting...")
    while True:
        log("[GitCommander] 🔍 Checking git status...")
        status = run_command("git status")
        if "nothing to commit" not in status:
            log("[GitCommander] 🔥 Changes detected, committing...")
            run_command('git add .')
            run_command('git commit -m "🚀 Savage auto-commit"')
            push_result = run_command("git push")
            log(f"[GitCommander] 🚀 Pushed to remote:\n{push_result}")
        else:
            log("[GitCommander] ✅ No changes to commit.")
        time.sleep(120)

if __name__ == "__main__":
    main()