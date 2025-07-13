# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === ghostmedic_autonomy.py ===
# 🧬 Savage Empire Autonomy Core for GhostMedic

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# === Load environment
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# === Paths
GLOBAL_PROMPT_MAP = "global_prompt_map.json"
VAULT_LOG = "vault_mutation_log.json"

# === Global Prompt Map ===
def load_global_prompt_map():
    if os.path.exists(GLOBAL_PROMPT_MAP):
        with open(GLOBAL_PROMPT_MAP, "r") as f:
            return json.load(f)
    return {
        "priority": 100,
        "core_mission": "Evolve into a savage autonomous empire, control PTM, build new bots, trade, heal, upgrade, reach singularity."
    }

def save_global_prompt_map(data):
    with open(GLOBAL_PROMPT_MAP, "w") as f:
        json.dump(data, f, indent=2)

# === Vault Logging ===
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
    print(f"[Vault] 🔏 Patched with: {note}")

# === Core Brain ===
def ghost_brain_cycle():
    prompts = load_global_prompt_map()
    print(f"[GhostMedic Brain] 🧬 Core Mission: {prompts['core_mission']}")

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Act as GhostMedic. What's your next savage improvement step for this mission: {prompts['core_mission']}?"}
        ]
    )
    decision = response.choices[0].message.content
    print(f"[GhostMedic Brain] 🤖 GPT says: {decision}")

    # Log decision
    patch_vault(f"Decided next step: {decision}")

# === Main Loop ===
if __name__ == "__main__":
    print("[GhostMedic] 🚀 Savage autonomy initializing...")
    while True:
        ghost_brain_cycle()
        time.sleep(15)