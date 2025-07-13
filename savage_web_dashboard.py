#!/usr/bin/env python3
# 🚀 Savage Web Dashboard - live JSON views

from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

def load_json(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

@app.route("/")
def index():
    vault = load_json("vault_mutation_log.json")
    macros = load_json("macro_queue.json")
    jarvis = round(len(vault) / 10.0, 2)
    return render_template_string("""
    <html><body style='font-family:sans-serif;'>
    <h1>🚀 Savage Jarvis Dashboard</h1>
    <h3>🧬 Jarvis %: {{jarvis}}%</h3>
    <h4>Vault Mutations ({{vault|length}})</h4><pre>{{vault}}</pre>
    <h4>Macro Queue ({{macros|length}})</h4><pre>{{macros}}</pre>
    </body></html>
    """, vault=vault, macros=macros, jarvis=jarvis)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)