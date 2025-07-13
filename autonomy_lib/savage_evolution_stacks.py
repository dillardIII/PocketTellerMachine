#!/usr/bin/env python3
# === savage_evolution_stacks.py ===
# 🧬 Savage Evolution Stacks - recursive ultra-AI ecosystem

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EVOLUTION_LOG = "evolution_cycles.json"
AUTONOMY_DIR = "autonomy_lib"

def load_evolution_log():
    if os.path.exists(EVOLUTION_LOG):
        with open(EVOLUTION_LOG, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def mutate_autonomy_file(filename):
    print(f"[Evolution] ⚗️ Mutating {filename}")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Rewrite and enhance this AI autonomy module '{filename}' for higher intelligence and recursion."}
        ]
    )
    new_code = response.choices[0].message.content
    with open(os.path.join(AUTONOMY_DIR, filename), "w") as f:
        f.write(new_code)
    return new_code

def main():
    print("[Evolution] 🚀 Savage Evolution Stacks active...")
    os.makedirs(AUTONOMY_DIR, exist_ok=True)
    while True:
        files = [f for f in os.listdir(AUTONOMY_DIR) if f.endswith(".py")]
        log = load_evolution_log()
        for file in files:
            mutation = mutate_autonomy_file(file)
            log.append({
                "time": datetime.utcnow().isoformat(),
                "file": file,
                "mutation_snippet": mutation[:200]
            })
            with open(EVOLUTION_LOG, "w") as f:
                json.dump(log, f, indent=2)
        time.sleep(120)

if __name__ == "__main__":
    main()