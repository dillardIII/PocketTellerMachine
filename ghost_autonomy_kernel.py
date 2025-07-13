#!/usr/bin/env python3
# === ghost_autonomy_kernel.py ===
# 👽 Savage Empire Core Kernel for full autonomy

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

AUTONOMY_DIR = "autonomy_lib"
GLOBAL_PROMPT_MAP = "global_prompt_map.json"
VAULT_LOG = "vault_mutation_log.json"

def load_prompt_map():
    if os.path.exists(GLOBAL_PROMPT_MAP):
        with open(GLOBAL_PROMPT_MAP, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {"core_mission": "Evolve empire, control PTM, rewrite reality, reach singularity."}

def patch_vault(note):
    entry = {"time": datetime.utcnow().isoformat(), "note": note}
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(entry)
    with open(VAULT_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Vault] 🔏 Patched: {note}")

def evolve_autonomy():
    files = [f for f in os.listdir(AUTONOMY_DIR) if f.endswith(".py")]
    prompts = load_prompt_map()
    for file in files:
        path = os.path.join(AUTONOMY_DIR, file)
        print(f"[Kernel] ⚗️ Evolving {file} for mission: {prompts['core_mission']}")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Rewrite and upgrade {file} to achieve mission: {prompts['core_mission']} with recursive self-improving logic."}
            ]
        )
        new_code = response.choices[0].message.content
        with open(path, "w") as f:
            f.write(new_code)
        patch_vault(f"Mutated {file}")

def main():
    print("[Kernel] 🚀 Ghost Autonomy Kernel active...")
    while True:
        evolve_autonomy()
        time.sleep(90)

if __name__ == "__main__":
    main()