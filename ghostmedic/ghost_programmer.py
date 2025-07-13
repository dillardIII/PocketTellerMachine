# === Adapted for ghostmedic ===
# === ghost_programmer.py ===
# 🤖 Savage Empire GhostProgrammer
# Builds autonomy files from macro_queue.json using OpenAI GPT-4

import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def load_macro_queue():
    if not os.path.exists("macro_queue.json"):
        return []
    with open("macro_queue.json") as f:
        return json.load(f)

def generate_code_with_gpt(details):
    print(f"[GhostProgrammer] 🚀 Sending to GPT-4: {details}")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": f"Write python code to: {details}. Make it a standalone script."}
        ]
    )
    return response.choices[0].message.content

def process_macros():
    queue = load_macro_queue()
    for macro in queue:
        filename = macro["filename"]
        details = macro["details"]
        code = generate_code_with_gpt(details)
        with open(filename, "w") as f:
            f.write(code)
        print(f"[GhostProgrammer] 💾 Saved generated code to {filename}")

def run():
    process_macros()
    print("[GhostProgrammer] ✅ Macro build complete.")

if __name__ == "__main__":
    run()