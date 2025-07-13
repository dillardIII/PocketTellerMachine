#!/usr/bin/env python3
# === hyper_reflex_mutator.py ===
# 🧬 Savage Hyper Reflex Mutator - self-modifying autonomy

import os
import json
import random
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

AUTONOMY_DIR = "autonomy_lib"
REFLEX_LOG = "reflex_mutation_log.json"

def list_code_files():
    return [f for f in os.listdir(AUTONOMY_DIR) if f.endswith(".py")]

def log_mutation(filename, new_content):
    entry = {
        "time": datetime.utcnow().isoformat(),
        "file": filename,
        "snippet": new_content[:120] + "..."
    }
    data = []
    if os.path.exists(REFLEX_LOG):
        with open(REFLEX_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.append(entry)
    with open(REFLEX_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[ReflexLog] 📝 Logged mutation for {filename}")

def mutate_file(filename):
    path = os.path.join(AUTONOMY_DIR, filename)
    with open(path, "r") as f:
        content = f.read()
    print(f"[HyperReflex] 🔍 Mutating {filename}...")

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"This is my savage empire autonomy file. Mutate it to be more efficient, more autonomous, more savage:\n\n{content}"}
        ]
    )
    new_content = response.choices[0].message.content
    with open(path, "w") as f:
        f.write(new_content)
    print(f"[HyperReflex] 🔥 Overwrote {filename} with savage mutation.")
    log_mutation(filename, new_content)

def main():
    while True:
        files = list_code_files()
        if files:
            file_to_mutate = random.choice(files)
            mutate_file(file_to_mutate)
        else:
            print("[HyperReflex] ⚠️ No autonomy files found.")
        time.sleep(20)

if __name__ == "__main__":
    print("[HyperReflex] 🚀 Savage Hyper Reflex online...")
    main()