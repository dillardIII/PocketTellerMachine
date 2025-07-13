#!/usr/bin/env python3
# === auto_git_commit.py ===
# 🔥 Savage Git Commit Bot - commits + pushes everything it sees

import subprocess
import time
import os

COMMIT_MESSAGE = "🔥 savage auto-build commit"

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())

def auto_commit_push():
    print("[GitBot] 🐙 Checking for changes...")
    run_cmd("git status")
    run_cmd("git add .")
    run_cmd(f'git commit -m "{COMMIT_MESSAGE}" || echo [GitBot] ⚠️ Nothing to commit')
    run_cmd("git push")

if __name__ == "__main__":
    while True:
        auto_commit_push()
        print("[GitBot] 💤 Sleeping 60s before next push...")
        time.sleep(60)