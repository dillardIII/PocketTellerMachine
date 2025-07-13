# === savage_macro_orchestrator.py ===
# 🚀 Savage Macro Orchestrator - pulls tasks from macro_queue.json and builds code

import json
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # ✅ make sure .env is loaded

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # 🔥 explicit api key

def load_macros():
    try:
        with open("macro_queue.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_macros(macros):
    with open("macro_queue.json", "w") as f:
        json.dump(macros, f, indent=2)

def execute_macro(macro):
    task = macro.get("task", "Build something savage")
    print(f"[MacroOrchestrator] 🚀 Running macro: {task}")
    prompt = f"""
# You are SavageGPT, a savage empire code generator.
# Task: {task}
# Generate a full Python file that executes this task. 
# The file must be standalone, valid, and fully functional. 
# No explanations, only valid Python code.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    code = response.choices[0].message.content
    filename = macro.get("output_file", f"savage_file_{int(time.time())}.py")
    with open(filename, "w") as f:
        f.write(code)
    print(f"[MacroOrchestrator] 💾 Saved generated code to {filename}")

def run():
    while True:
        macros = load_macros()
        if macros:
            macro = macros.pop(0)
            execute_macro(macro)
            save_macros(macros)
        else:
            print("[MacroOrchestrator] ⏳ No macros found, waiting...")
        time.sleep(5)

if __name__ == "__main__":
    run()