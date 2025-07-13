#!/usr/bin/env python3
# === savage_swarm_builder.py ===
# 🐙 Savage Multi-AI Swarm Builder - GPT, Gemini (auto-catch), Replicate, Vault logs

import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load .env for all your keys
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")
REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

try:
    import google.generativeai as genai
    genai.configure(api_key=GOOGLE_GENAI_API_KEY)
    GEMINI_ENABLED = True
except (ImportError, Exception):
    genai = None
    GEMINI_ENABLED = False

try:
    import replicate
    REPLICATE_ENABLED = True
except ImportError:
    replicate = None
    REPLICATE_ENABLED = False

VAULT_LOG = "vault_mutation_log.json"

def patch_vault_log(note):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "note": note
    }
    if os.path.exists(VAULT_LOG):
        try:
            with open(VAULT_LOG, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
    else:
        data = []
    data.append(entry)
    with open(VAULT_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Vault] 🧬 Patched log: {note}")

def build_gpt4_module():
    print("[SwarmBuilder] 🤖 GPT-4 building savage module...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Write a Python script that prints 'Savage GPT-4 swarm module operational'."}
        ]
    )
    code = response.choices[0].message.content
    filename = f"swarm_gpt4_{int(time.time())}.py"
    with open(filename, "w") as f:
        f.write(code)
    patch_vault_log(f"Generated GPT-4 swarm file: {filename}")
    print(f"[SwarmBuilder] 💾 Saved GPT-4 file: {filename}")

def build_gemini_module():
    if not GEMINI_ENABLED:
        print("[SwarmBuilder] ⚠️ Google GenAI not installed or configured.")
        return
    try:
        print("[SwarmBuilder] 🤖 Gemini building savage module...")
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content("Write a Python script that prints 'Savage Gemini swarm module active.'")
        filename = f"swarm_gemini_{int(time.time())}.py"
        with open(filename, "w") as f:
            f.write(response.text)
        patch_vault_log(f"Generated Gemini swarm file: {filename}")
        print(f"[SwarmBuilder] 💾 Saved Gemini file: {filename}")
    except Exception as e:
        patch_vault_log(f"Gemini failed: {e}")
        print(f"[SwarmBuilder] ⚠️ Gemini failed: {e}")

def build_replicate_module():
    if not REPLICATE_ENABLED:
        print("[SwarmBuilder] ⚠️ Replicate not installed.")
        return
    try:
        print("[SwarmBuilder] 🤖 Replicate building savage module...")
        output = replicate.run(
            "stability-ai/stable-codegen:latest",
            input={"prompt": "Write a Python file that prints 'Savage Replicate swarm module engaged.'"}
        )
        filename = f"swarm_replicate_{int(time.time())}.py"
        with open(filename, "w") as f:
            f.write(output)
        patch_vault_log(f"Generated Replicate swarm file: {filename}")
        print(f"[SwarmBuilder] 💾 Saved Replicate file: {filename}")
    except Exception as e:
        patch_vault_log(f"Replicate failed: {e}")
        print(f"[SwarmBuilder] ⚠️ Replicate failed: {e}")

def main():
    print("[SwarmBuilder] 🐙 Savage Multi-AI Swarm Builder starting up...")
    while True:
        build_gpt4_module()
        build_gemini_module()
        build_replicate_module()
        print("[SwarmBuilder] ⏳ Sleeping before next savage rotation...")
        time.sleep(30)

if __name__ == "__main__":
    main()