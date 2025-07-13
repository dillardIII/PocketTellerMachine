#!/usr/bin/env python3
# === macro_queue_consumer.py ===
# 🧬 Savage Macro Queue Consumer - auto-feeds macros into GPT builder

import json
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("🚨 OPENAI_API_KEY not found in environment or .env file!")

client = OpenAI(api_key=OPENAI_API_KEY)

MACRO_QUEUE = "macro_queue.json"
VAULT_LOG = "vault_macro_log.json"

def patch_vault_log(note):
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append({"time": time.time(), "note": note})
    with open(VAULT_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[VaultPatch] 🧬 Logged macro: {note}")

def consume_macros():
    if not os.path.exists(MACRO_QUEUE):
        return

    with open(MACRO_QUEUE, "r") as f:
        try:
            queue = json.load(f)
        except json.JSONDecodeError:
            queue = []

    if not queue:
        return

    new_queue = []
    for macro in queue:
        if macro.get("action") == "generate_or_repair_file":
            details = macro.get("details", "create something savage")
            print(f"[MacroConsumer] 🚀 Sending to GPT: {details}")
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": f"Auto-generate Python file: {details}"}
                ]
            )
            code = response.choices[0].message.content
            filename = f"savage_macro_{int(time.time())}.py"
            with open(filename, "w") as f:
                f.write(code)
            print(f"[MacroConsumer] 💾 Saved: {filename}")
            patch_vault_log(f"Built {filename} for task: {details}")
        else:
            print(f"[MacroConsumer] ⚠️ Unknown macro, skipping: {macro}")
            new_queue.append(macro)

    with open(MACRO_QUEUE, "w") as f:
        json.dump(new_queue, f, indent=2)

def main():
    print("[MacroConsumer] 🔥 Savage Macro Consumer starting up...")
    while True:
        consume_macros()
        time.sleep(5)

if __name__ == "__main__":
    main()