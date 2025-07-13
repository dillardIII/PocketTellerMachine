#!/usr/bin/env python3
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/wallets')
def wallets():
    with open('wallet_hunts.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/ptm')
def ptm():
    with open('ptm_heals.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/vault')
def vault():
    with open('vault_mutation_log.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)