#!/usr/bin/env python3
# === savage_bridge_autobuilder.py ===
# 🧬 Savage Empire Bridge AutoBuilder with JSON, TAS parsing, GPT file writes, and explicit OpenAI key

import os
import json
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load .env into os.environ
load_dotenv()

# Explicit OpenAI client with key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_tas_queue():
    """Load tasks from JSON macro queue file."""
    if os.path.exists("macro_queue.json"):
        with open("macro_queue.json", "r") as f:
            return json.load(f)
    return []

def mark_done(task, status="completed"):
    """Append to mutation log to keep track of generated files."""
    log_entry = {
        "task": task,
        "status": status,
        "time": int(time.time())
    }
    if os.path.exists("mutation_log.json"):
        with open("mutation_log.json", "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append(log_entry)
    with open("mutation_log.json", "w") as f:
        json.dump(data, f, indent=2)

def generate_code(task):
    """Use OpenAI GPT to generate code for a given task and write to file."""
    print(f"[AutoBuilder] 🚀 Processing task: {task}")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Create or repair code file for: {task}."}
        ]
    )
    code = response.choices[0].message.content
    filename = f"savage_file_{int(time.time())}.py"
    with open(filename, "w") as f:
        f.write(code)
    print(f"[AutoBuilder] 💾 Saved generated code to {filename}")
    mark_done(task, "generated")
    return filename

def main_loop():
    """Main loop to watch the TAS queue and build autonomy files."""
    while True:
        tasks = load_tas_queue()
        if tasks:
            for task in tasks:
                generate_code(task)
            # Clear queue after processing
            with open("macro_queue.json", "w") as f:
                json.dump([], f)
        else:
            print("[AutoBuilder] 🔄 No tasks in queue. Waiting...")
        time.sleep(5)

if __name__ == "__main__":
    print("[AutoBuilder] 🧬 Savage Bridge AutoBuilder starting up...")
    main_loop()