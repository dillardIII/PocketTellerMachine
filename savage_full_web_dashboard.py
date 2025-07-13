#!/usr/bin/env python3
from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            try: return json.load(f)
            except: return []
    return []

@app.route("/")
def index():
    vault = load_json("vault_mutation_log.json")
    macro = load_json("macro_queue.json")
    jarvis = min(100, len(vault) / 10)
    html = f"""
    <html><body style='background:black;color:#0f0;font-family:monospace;'>
    <h1>🚀 Savage Empire Dashboard</h1>
    <p>🧬 Jarvis Level: {jarvis:.2f}%</p>
    <h2>Vault Mutations</h2><pre>{json.dumps(vault[-10:], indent=2)}</pre>
    <h2>Macro Queue</h2><pre>{json.dumps(macro[-10:], indent=2)}</pre>
    </body></html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)