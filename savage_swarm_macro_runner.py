#!/usr/bin/env python3
# === savage_swarm_macro_runner.py ===
# 🐙 Savage Swarm Macro Runner - reads inbox JSON tasks, triggers GPT, Gemini, Replicate

import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# === Load all your env vars ===
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")
REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

try:
    import google.generativeai as genai
    genai.configure(api_key=GOOGLE_GENAI_API_KEY)
    GEMINI_ENABLED = True
except:
    GEMINI_ENABLED = False

try:
    import replicate
    REPLICATE_ENABLED = True
except:
    REPLICATE_ENABLED = False

INBOX = "inbox"
VAULT_LOG = "vault_mutation_log.json"

os.makedirs(INBOX, exist_ok=True)

def patch_vault_log(note):
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
    print(f"[VaultPatch] 🧬 Logged: {note}")

def run_gpt_task(cmd):
    print("[MacroRunner] 🤖 Sending to GPT...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": cmd}]
    )
    code = response.choices[0].message.content
    fname = f"swarm_gpt_{int(time.time())}.py"
    with open(fname, "w") as f:
        f.write(code)
    patch_vault_log(f"Generated via GPT: {fname}")

def run_gemini_task(cmd):
    if not GEMINI_ENABLED:
        print("[MacroRunner] ⚠️ Gemini not installed.")
        return
    try:
        print("[MacroRunner] 🤖 Sending to Gemini...")
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(cmd)
        fname = f"swarm_gemini_{int(time.time())}.py"
        with open(fname, "w") as f:
            f.write(response.text)
        patch_vault_log(f"Generated via Gemini: {fname}")
    except Exception as e:
        patch_vault_log(f"Gemini failed: {e}")
        print(f"[MacroRunner] ⚠️ Gemini failed: {e}")

def run_replicate_task(cmd):
    if not REPLICATE_ENABLED:
        print("[MacroRunner] ⚠️ Replicate not installed.")
        return
    try:
        print("[MacroRunner] 🤖 Sending to Replicate...")
        output = replicate.run(
            "stability-ai/stable-codegen:latest",
            input={"prompt": cmd}
        )
        fname = f"swarm_replicate_{int(time.time())}.py"
        with open(fname, "w") as f:
            f.write(output)
        patch_vault_log(f"Generated via Replicate: {fname}")
    except Exception as e:
        patch_vault_log(f"Replicate failed: {e}")
        print(f"[MacroRunner] ⚠️ Replicate failed: {e}")

def handle_macro(task):
    cmd = task.get("command", "")
    print(f"[MacroRunner] 📝 Command: {cmd}")

    # Dispatch to all 3 models
    run_gpt_task(cmd)
    run_gemini_task(cmd)
    run_replicate_task(cmd)

def main():
    print("[MacroRunner] 🐙 Watching inbox for macros...")
    while True:
        files = os.listdir(INBOX)
        for file in files:
            path = os.path.join(INBOX, file)
            try:
                with open(path, "r") as f:
                    task = json.load(f)
                if task.get("task") == "voice_macro":
                    handle_macro(task)
            except Exception as e:
                print(f"[MacroRunner] ⚠️ Failed to process {file}: {e}")
            finally:
                os.remove(path)
                print(f"[MacroRunner] 🗑️ Removed {file}")
        time.sleep(5)

if __name__ == "__main__":
    main()