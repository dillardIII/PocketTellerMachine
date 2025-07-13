#!/usr/bin/env python3
# === savage_git_webhook_listener.py ===
# 🚀 Auto-pulls on any remote push

from flask import Flask, request
import subprocess
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.json
    if payload:
        print(f"[Webhook] 🚀 GitHub push detected at {payload.get('repository', {}).get('full_name', 'unknown')}")
        subprocess.run(["python3", "savage_git_auto_rebase.py"])
        subprocess.run(["python3", "savage_global_sync_chain.py"])
    return json.dumps({"status": "ok"})

if __name__ == "__main__":
    print("[Webhook] 🌐 Starting savage webhook listener on port 5000...")
    app.run(host="0.0.0.0", port=5000)