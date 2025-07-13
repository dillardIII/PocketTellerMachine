#!/usr/bin/env python3
# === savage_realtime_dashboard.py ===
# 🚀 Savage Realtime Dashboard - Watch your empire live.

from flask import Flask, render_template_string
import json
import os
from datetime import datetime
import time

app = Flask(__name__)

VAULT_LOG = "vault_mutation_log.json"
MACRO_QUEUE = "macro_queue.json"

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Savage Realtime Dashboard</title>
    <meta http-equiv="refresh" content="3">
    <style>
        body { background: black; color: #0f0; font-family: monospace; }
        h1,h2,h3 { color: #f00; }
        .block { margin: 20px 0; padding: 10px; border: 1px solid #0f0; }
    </style>
</head>
<body>
    <h1>🚀 Savage Realtime Dashboard</h1>
    <div class="block">
        <h2>Vault Mutations ({{ vault|length }})</h2>
        {% for entry in vault[-10:] %}
            <p>[{{ entry.time }}] {{ entry.note or entry.findings or entry.task }}</p>
        {% endfor %}
    </div>
    <div class="block">
        <h2>Macro Queue ({{ macros|length }})</h2>
        {% for task in macros[-10:] %}
            <p>[{{ task.time }}] {{ task.task }}</p>
        {% endfor %}
    </div>
    <div class="block">
        <h2>Jarvis % Estimate: {{ jarvis }}%</h2>
    </div>
</body>
</html>
"""

def read_json(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

def calculate_jarvis(vault):
    # Example: Each vault entry = 0.1% towards Jarvis
    return round(len(vault) * 0.1, 2)

@app.route("/")
def index():
    vault = read_json(VAULT_LOG)
    macros = read_json(MACRO_QUEUE)
    jarvis = calculate_jarvis(vault)
    return render_template_string(TEMPLATE, vault=vault, macros=macros, jarvis=jarvis)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)