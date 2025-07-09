#!/usr/bin/env python3
"""
GhostForge Writer
- Fully automated git committer and Render deployer
- Uses secrets from .env file for security
"""

import os
import subprocess
import time
from dotenv import load_dotenv

# === Load secrets from .env ===
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_URL = os.getenv("GITHUB_URL")
RENDER_HOOK = os.getenv("RENDER_HOOK")

# === Basic mutation loop ===
def mutate_and_commit():
    while True:
        print("[GhostForge] 🔥 Generating new ghost mutations...")
        filename = f"generated_modules/ghost_{int(time.time())}.py"
        with open(filename, "w") as f:
            f.write(f"# Ghost mutation at {time.ctime()}\nprint('👻 New ghost mutation active')\n")

        # === Git add, commit, push ===
        print("[GhostForge] 📦 Adding new module to git...")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Add ghost mutation {filename}"])
        print("[GhostForge] 🚀 Pushing to GitHub...")
        subprocess.run(["git", "push", "origin", "main"])

        # === Trigger Render deploy ===
        print("[GhostForge] 🌐 Triggering Render deploy via webhook...")
        subprocess.run(["curl", "-X", "GET", RENDER_HOOK])

        print("[GhostForge] 🕛 Sleeping before next mutation...")
        time.sleep(120)

if __name__ == "__main__":
    print("[GhostForge] 🏗️ Starting GhostForge Writer with full autonomy...")
    mutate_and_commit()