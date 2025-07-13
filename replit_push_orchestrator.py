#!/usr/bin/env python3
# === replit_push_orchestrator.py ===
# 🚀 Savage Replit Push Orchestrator - pushes evolved code to your Replit

import os
import json
import time
import requests
from datetime import datetime

OUTBOX_DIR = "outbox"
REPLIT_PROJECT_URL = os.getenv("REPLIT_PROJECT_URL")  # should be like https://api.replit.com/v0/projects/your-id/files
REPLIT_API_KEY = os.getenv("REPLIT_API_KEY")

PUSH_LOG = "replit_push_log.json"

def push_file_to_replit(file_path, target_path):
    headers = {
        "Authorization": f"Bearer {REPLIT_API_KEY}",
        "Content-Type": "application/json"
    }
    with open(file_path, "r") as f:
        content = f.read()
    payload = {
        "path": target_path,
        "content": content
    }
    response = requests.post(REPLIT_PROJECT_URL, headers=headers, json=payload)
    return response.status_code == 200

def log_push(file, status):
    entry = {"time": datetime.utcnow().isoformat(), "file": file, "status": status}
    data = []
    if os.path.exists(PUSH_LOG):
        with open(PUSH_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass
    data.append(entry)
    with open(PUSH_LOG, "w") as f:
        json.dump(data, f, indent=2)

def main():
    print("[ReplitPush] 🚀 Savage Replit Push Orchestrator running...")
    while True:
        files = [f for f in os.listdir(OUTBOX_DIR) if f.endswith(".py")]
        for file in files:
            full_path = os.path.join(OUTBOX_DIR, file)
            print(f"[ReplitPush] 🔥 Pushing {file} to Replit...")
            success = push_file_to_replit(full_path, f"/autonomy/{file}")
            log_push(file, "success" if success else "failed")
            if success:
                os.remove(full_path)
        time.sleep(60)

if __name__ == "__main__":
    main()