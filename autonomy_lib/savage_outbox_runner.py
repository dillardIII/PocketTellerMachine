#!/usr/bin/env python3
# === savage_outbox_runner.py ===
# 🔥 Savage Outbox Runner w/ GPT+ & Vault Patch + explicit ENV loader

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load .env explicitly
load_dotenv()

OUTBOX = "outbox"
VAULT_LOG = "vault_mutation_log.json"

# Grab OPENAI key from .env or system env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("🚨 OPENAI_API_KEY not found in environment or .env file!")

client = OpenAI(api_key=OPENAI_API_KEY)

def patch_vault_log(task_desc):
    """
    Logs every mutation or GPT operation into a vault log for transparency and replay.
    """
    vault_record = {
        "timestamp": datetime.utcnow().isoformat(),
        "task": task_desc
    }
    if os.path.exists(VAULT_LOG):
        try:
            with open(VAULT_LOG, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []

    data.append(vault_record)
    with open(VAULT_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[VaultPatch] 🧬 Logged mutation: {task_desc}")

def handle_task(task):
    """
    Handles specific task commands, right now supports build_savage_ai.
    """
    print(f"[OutboxRunner] 🧠 Handling task: {task}")
    if isinstance(task, dict) and task.get("task") == "build_savage_ai":
        print("[OutboxRunner] 🚀 Sending to GPT to generate savage AI module...")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": "Write a savage AI Python module that prints a welcome and current timestamp."}
            ]
        )
        code = response.choices[0].message.content
        filename = f"savage_ai_{int(time.time())}.py"
        with open(filename, "w") as f:
            f.write(code)
        print(f"[OutboxRunner] 💾 Saved new savage file: {filename}")
        patch_vault_log(f"Generated file {filename} via GPT-4")
    else:
        print(f"[OutboxRunner] ⚠️ Unrecognized task or format: {task}")

def process_file(filepath):
    """
    Loads and parses outbox file content as JSON. Falls back to wrapping text.
    """
    try:
        with open(filepath, "r") as f:
            content = f.read()
        print(f"[OutboxRunner] 📦 Processing {filepath}:")
        print(content)

        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            data = {"task": "unknown", "content": content}

        handle_task(data)

    except Exception as e:
        print(f"[OutboxRunner] ⚠️ Failed processing {filepath}: {e}")
    finally:
        os.remove(filepath)
        print(f"[OutboxRunner] 🗑️ Removed {filepath}")

def main():
    """
    Main loop that continuously scans the outbox folder for JSON or text files.
    """
    os.makedirs(OUTBOX, exist_ok=True)
    print("[OutboxRunner] 🔥 Watching outbox for tasks...")

    while True:
        files = os.listdir(OUTBOX)
        for file in files:
            process_file(os.path.join(OUTBOX, file))
        time.sleep(4)

if __name__ == "__main__":
    main()