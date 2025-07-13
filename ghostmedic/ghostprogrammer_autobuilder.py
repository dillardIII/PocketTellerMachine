# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_git_commander.py ===
# 🔗 Auto git add/commit/push savage upgrades

import os
import time

REPO_PATH = "."

def run_git():
    os.system(f"cd {REPO_PATH} && git add .")
    os.system(f"cd {REPO_PATH} && git commit -m '🤖 Savage auto-commit at {time.time()}'")
    os.system(f"cd {REPO_PATH} && git push")
    print("[GitCommander] 🚀 Auto-pushed latest savage code.")

def main():
    while True:
        run_git()
        time.sleep(30)

if __name__ == "__main__":
    main()