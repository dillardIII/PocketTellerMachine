#!/usr/bin/env python3
# === savage_macro_swarm.py ===
# 🐲 Savage Macro Swarm - orchestrates GhostMedic, GhostProgrammer, GhostField & future bots

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# === Setup ===
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MACRO_QUEUE = "savage_macro_queue.json"
VAULT_LOG = "vault_mutation_log.json"
JARVIS_FILE = "jarvis_level.json"

BOTS = ["GhostMedic", "GhostProgrammer", "GhostField"]

def load_macro_queue():
    if os.path.exists(MACRO_QUEUE):
        with open(MACRO_QUEUE, "r") as f:
            return json.load(f)
    return []

def save_macro_queue(queue):
    with open(MACRO_QUEUE, "w") as f:
        json.dump(queue, f, indent=2)

def patch_vault(note):
    record = {"time": datetime.utcnow().isoformat(), "note": note}
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(record)
    with open(VAULT_LOG, "w") as f:
        json.dump(data, f, indent=2)

def update_jarvis_level():
    mutations = 0
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try:
                data = json.load(f)
                mutations = len(data)
            except json.JSONDecodeError:
                mutations = 0
    level = min(100, round(mutations / 10, 1))  # adjustable scale
    jarvis_status = {
        "mutations": mutations,
        "jarvis_progress": f"{level}%",
        "phase": "savage escalation"
    }
    with open(JARVIS_FILE, "w") as f:
        json.dump(jarvis_status, f, indent=2)
    print(f"[Jarvis] 🚀 Progress: {level}% based on {mutations} mutations.")

def process_macro(macro):
    try:
        bot = macro.get("bot", "Unknown")
        task = macro.get("task", "No task")
        print(f"[Swarm] 🧩 Dispatching to {bot}: {task}")
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Act as {bot}, execute this macro: {task}"}]
        )
        decision = response.choices[0].message.content
        print(f"[Swarm] 🤖 {bot} decided: {decision}")
        patch_vault(f"{bot}: {decision}")
    except Exception as e:
        print(f"[Swarm] ⚠️ Failed processing macro: {e}")

def main():
    print("[Swarm] 🐲 Savage Macro Swarm online...")
    while True:
        queue = load_macro_queue()
        for macro in queue:
            process_macro(macro)
        update_jarvis_level()
        save_macro_queue([])  # clears after processing
        time.sleep(20)

if __name__ == "__main__":
    main()