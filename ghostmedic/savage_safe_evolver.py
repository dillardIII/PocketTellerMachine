# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_safe_evolver.py ===
# 🛡 Safe Savage Evolver: upgrades empire only with validated improvements

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

VAULT_LOG = "vault_safe_mutations.json"

def log_upgrade(note):
    entry = {"time": datetime.utcnow().isoformat(), "note": note}
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try: data = json.load(f)
            except json.JSONDecodeError: data = []
    else:
        data = []
    data.append(entry)
    with open(VAULT_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Vault] 🔏 Logged safe upgrade: {note}")

def evolve_safely():
    print("[Evolver] 🚀 Requesting targeted improvements from GPT-4...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Improve my AI empire by making strategic, stable upgrades only. Ensure logic is sound, add integrity checks, no reckless mutations."}
        ]
    )
    decision = response.choices[0].message.content
    print(f"[Evolver] 🤖 GPT suggests: {decision}")
    log_upgrade(f"Safe evolution: {decision}")

def main():
    print("[Evolver] 🧬 Safe savage evolver started.")
    while True:
        evolve_safely()
        time.sleep(30)

if __name__ == "__main__":
    main()