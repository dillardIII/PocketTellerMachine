#!/usr/bin/env python3
# === savage_git_auto_rebase.py ===
# 💀 Savage Empire Git Auto-Rebase Macro
# Fully autonomous rebase + commit + push with minimal human intervention.

import os
import subprocess
import time
from datetime import datetime

REPO_PATH = "."  # or your specific subdir

def run(cmd):
    print(f"[GitMacro] 🛠️ Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result

def check_unstaged_changes():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=REPO_PATH,
        capture_output=True,
        text=True
    )
    return bool(result.stdout.strip())

def auto_commit_changes():
    timestamp = datetime.utcnow().isoformat()
    run(f"git add .")
    run(f"git commit -m '💀 Auto-commit at {timestamp}'")

def auto_rebase_pull():
    print("[GitMacro] 🔄 Pulling with rebase from remote...")
    result = run("git pull --rebase")
    if "CONFLICT" in result.stdout or "CONFLICT" in result.stderr:
        print("[GitMacro] ⚠️ Conflict detected! Running force resolution (keep local)...")
        run("git add .")
        run(f"git commit -m '⚔️ Auto-resolve rebase conflict by keeping local'")
        print("[GitMacro] ✅ Conflicts staged. Continuing rebase...")
        run("git rebase --continue")

def push_changes():
    print("[GitMacro] 🚀 Pushing to remote...")
    run("git push")

def main():
    print("[GitMacro] 🔥 Savage Git Auto-Rebase Macro starting...")
    os.chdir(REPO_PATH)

    if check_unstaged_changes():
        print("[GitMacro] ✍️ Local changes detected. Auto-committing...")
        auto_commit_changes()
    else:
        print("[GitMacro] ✅ No local changes. Clean state.")

    auto_rebase_pull()
    push_changes()
    print("[GitMacro] 💀 Savage auto-rebase complete.")

if __name__ == "__main__":
    while True:
        main()
        print("[GitMacro] ⏳ Sleeping before next auto-check...")
# 🧬 Mutation at 2025-07-13T11:34:17.181516
        time.sleep(300)  # check every 5 minutes