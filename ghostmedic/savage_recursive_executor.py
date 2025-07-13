# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_recursive_executor.py ===
# 🔥 Savage Recursive Executor with Macro Consumer, Global Director & Mutation Historian

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MACRO_QUEUE = "macro_queue.json"
HISTORIAN_LOG = "savage_historian.json"
AUTONOMY_DIR = "autonomy_lib"

def load_macros():
    if os.path.exists(MACRO_QUEUE):
        with open(MACRO_QUEUE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def append_historian(entry):
    data = []
    if os.path.exists(HISTORIAN_LOG):
        with open(HISTORIAN_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.append(entry)
    with open(HISTORIAN_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Historian] 📝 Logged: {entry['task']}")

def execute_macro(macro):
    task = macro.get("task", "unknown")
    details = macro.get("details", "")
    print(f"[RecursiveExecutor] 🧩 Executing macro: {task} - {details}")

    # GPT-driven mutation or generation
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Act as a savage empire AI. Execute macro: {task}. Details: {details}. Write a small Python file as your output."}
        ]
    )
    code = response.choices[0].message.content

    filename = os.path.join(AUTONOMY_DIR, f"savage_{task.replace(' ','_')}_{int(time.time())}.py")
    with open(filename, "w") as f:
        f.write(code)
    print(f"[RecursiveExecutor] 💾 Saved to: {filename}")

    # Log to historian
    append_historian({
        "time": datetime.utcnow().isoformat(),
        "task": f"{task} - {details}",
        "file": filename
    })

def main():
    os.makedirs(AUTONOMY_DIR, exist_ok=True)
    while True:
        macros = load_macros()
        if macros:
            for macro in macros:
                execute_macro(macro)
            with open(MACRO_QUEUE, "w") as f:
                json.dump([], f)  # Clear after processing
        else:
            print("[RecursiveExecutor] ⏳ No macros found. Waiting...")
        time.sleep(10)

if __name__ == "__main__":
    print("[RecursiveExecutor] 🚀 Savage Recursive Executor online...")
    main()