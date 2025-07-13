#!/usr/bin/env python3
from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route("/")
def index():
    try:
        with open("vault_mutation_log.json") as f:
            data = f.readlines()[-10:]
    except:
        data = ["No vault data yet."]
    return render_template_string("""
    <h1>💀 Savage Vault Dashboard</h1>
    <pre>{{data}}</pre>
    """, data=data)

app.run(host="0.0.0.0", port=5000)