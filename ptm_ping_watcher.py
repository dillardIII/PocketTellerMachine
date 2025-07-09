#!/usr/bin/env python3
"""
PTM Live Ping Watcher
- Keeps an eye on PTM health
- If recovery mode detected, triggers self-heal
- Logs results for your empire
"""

import json
import time
import os
from datetime import datetime

PTM_CONFIG_PATH = "path/to/your/ptm/config.json"  # 🔥 <== adjust this to your PTM's config.json location
WATCH_INTERVAL = 15

def log_event(message):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ptm_ping_log.txt", "a") as f:
        f.write(f"[{ts}] {message}\n")
    print(f"[PTM Watcher] {message}")

def check_ptm_health():
    try:
        with open(PTM_CONFIG_PATH, "r") as f:
            config = json.load(f)
        if config.get("recovery_mode", False):
            log_event("⚠️ PTM in recovery mode! Triggering self-heal.")
            return False
        else:
            log_event("✅ PTM healthy.")
            return True
    except Exception as e:
        log_event(f"❌ Error reading PTM config: {e}")
        return False

def trigger_self_heal():
    log_event("🔧 Running GhostMedic heal command on PTM...")
    # 🔥 Example: Call a bash script, or another python that does your normal patch
    os.system("python3 ghostmedic.py")  # adjust to your actual repair launcher

def main_loop():
    while True:
        healthy = check_ptm_health()
        if not healthy:
            trigger_self_heal()
        time.sleep(WATCH_INTERVAL)

if __name__ == "__main__":
    log_event("🚀 Starting PTM live ping watcher...")
    main_loop()