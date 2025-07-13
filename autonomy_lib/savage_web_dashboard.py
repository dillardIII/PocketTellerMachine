#!/usr/bin/env python3
# === savage_web_dashboard.py ===
# 🌐 Savage Web Dashboard for PTM Empire

from flask import Flask, render_template_string, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    vault = {}
    try:
        with open("vault_macro_log.json", "r") as f:
            vault = json.load(f)
    except:
        vault = []

    macro_queue = []
    try:
        with open("macro_queue.json", "r") as f:
            macro_queue = json.load(f)
    except:
        macro_queue = []

    return render_template_string("""
    <html>
    <head>
        <title>Savage Empire Dashboard</title>
        <style>
            body { background: #111; color: #0f0; font-family: monospace; }
            h1 { color: #f0f; }
            pre { background: #222; padding: 10px; }
        </style>
    </head>
    <body>
        <h1>🔥 Savage Empire Dashboard</h1>
        <h2>Macro Queue</h2>
        <pre>{{ macro_queue }}</pre>
        <h2>Vault Mutation Log</h2>
        <pre>{{ vault }}</pre>
    </body>
    </html>
    """, macro_queue=json.dumps(macro_queue, indent=2),
         vault=json.dumps(vault, indent=2))

@app.route("/api/status")
def api_status():
    try:
        with open("vault_macro_log.json", "r") as f:
            vault = json.load(f)
    except:
        vault = []

    try:
        with open("macro_queue.json", "r") as f:
            macro_queue = json.load(f)
    except:
        macro_queue = []

    return jsonify({
        "vault_log": vault,
        "macro_queue": macro_queue
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)