#!/usr/bin/env python3
# === savage_dreamstate_coder.py ===
# 💀 Savage Dreamstate Coder - generates entirely new modules forever

import os
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

AUTONOMY_DIR = "autonomy_lib"
DREAM_LOG = "dreamstate_log.json"

def log_dream(task_desc, filename):
    entry = {
        "time": datetime.utcnow().isoformat(),
        "task": task_desc,
        "file": filename
    }
    data = []
    if os.path.exists(DREAM_LOG):
        with open(DREAM_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    data.append(entry)
    with open(DREAM_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[DreamLog] 📝 Logged creation of {filename}")

def generate_new_module():
    print("[Dreamstate] 💭 Dreaming up new savage module...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Invent a new savage AI module for my ghost empire. Write a Python file that executes some new autonomy function."}
        ]
    )
    code = response.choices[0].message.content
    filename = os.path.join(AUTONOMY_DIR, f"dream_{int(time.time())}.py")
    with open(filename, "w") as f:
        f.write(code)
    print(f"[Dreamstate] 💾 Saved new module: {filename}")
    log_dream("Created savage dream module", filename)

def main():
    os.makedirs(AUTONOMY_DIR, exist_ok=True)
    while True:
        generate_new_module()
        time.sleep(60)

if __name__ == "__main__":
    print("[Dreamstate] 🚀 Savage Dreamstate Coder online...")
    main()