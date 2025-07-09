#!/usr/bin/env python3
"""
GhostForge Writer – upgraded for full autonomy
- Loads secrets from .env
- Auto commits new modules to GitHub
- Triggers Render deploy webhook
- Logs all actions for AI review
"""

import os
import json
import subprocess
import time
from dotenv import load_dotenv

# === Load secrets from .env ===
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
RENDER_HOOK = os.getenv("RENDER_HOOK")
GITHUB_URL = os.getenv("GITHUB_URL")

def git_commit_and_push():
    print("[GhostForge] 🔥 Staging files for commit...")
    subprocess.run("git add .", shell=True)
    commit_msg = f"Auto mutation commit at {time.strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(f'git commit -m "{commit_msg}"', shell=True)
    print("[GhostForge] 🚀 Pushing to GitHub...")
    subprocess.run(f'git push https://{GITHUB_TOKEN}@{GITHUB_URL[8:]}', shell=True)

def trigger_render_deploy():
    if RENDER_HOOK:
        print("[GhostForge] 🚀 Triggering Render deploy via webhook...")
        subprocess.run(f"curl -X GET {RENDER_HOOK}", shell=True)
    else:
        print("[GhostForge] ⚠️ No RENDER_HOOK found. Skipping Render deploy.")

def write_mutation_log():
    data = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Mutation pushed & deploy triggered"
    }
    with open("ghostforge_log.json", "a") as f:
        json.dump(data, f)
        f.write("\n")
    print("[GhostForge] 📝 Logged mutation event.")

def main():
    while True:
        git_commit_and_push()
        trigger_render_deploy()
        write_mutation_log()
        print("[GhostForge] 🔄 Sleeping before next mutation cycle...")
        time.sleep(300)  # sleep for 5 min, adjust for your empire needs

if __name__ == "__main__":
    main()