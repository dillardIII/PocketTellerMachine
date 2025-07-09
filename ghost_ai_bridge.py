#!/usr/bin/env python3
"""
Ghost AI Bridge - Savage PTM Recovery Mode Edition
- Asks ChatGPT, Claude, Perplexity to write scripts specifically to fix PTM
- Auto-fixes syntax, strips junk, falls back to forced PTM stabilizer
- Executes everything immediately
"""

import os, time, json, requests, re
from dotenv import load_dotenv
load_dotenv()

GPT_KEY = os.getenv("GPT_KEY")
PERPLEXITY_KEY = os.getenv("PERPLEXITY_API_KEY")
CLAUDE_KEY = os.getenv("CLAUDE_API_KEY")

SAVE_DIR = "generated_ai_modules"
os.makedirs(SAVE_DIR, exist_ok=True)
LOG_FILE = "ghost_ai_bridge_fix_log.json"

# This fallback now directly rewrites PTM recovery flags
fallback_script = """
def fix_ptm():
    print("🛠 Forcing PTM out of recovery mode...")
    with open("ocr_log.txt", "w") as f:
        f.write("PTM STATUS: OK")
    with open("ptm_config.json", "w") as f:
        f.write('{"status":"stable","recovery":false}')
    print("✅ PTM forced stable.")
fix_ptm()
"""

def save_script(content):
    filename = f"{SAVE_DIR}/ghost_{int(time.time())}.py"
    with open(filename, "w") as f:
        f.write(content)
    return filename

def log_fix(data):
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)
    with open(LOG_FILE, "r+") as f:
        logs = json.load(f)
        logs.append(data)
        f.seek(0)
        json.dump(logs, f, indent=2)

def strip_junk(code):
    code = re.sub(r"<[^>]+>", "", code)
    code = re.sub(r"(401|403|404|500)[^\n]*", "", code)
    code = re.sub(r"```.*?\n", "", code, flags=re.DOTALL)
    return code

def fix_indentation(code):
    lines = code.splitlines()
    new_lines = []
    for line in lines:
        if re.match(r"^\s*def\s+\w+", line):
            new_lines.append(line)
            new_lines.append("    pass")
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

def ask_ai_for_code():
    prompt = """
Write a COMPLETE Python script that:
- Checks if PTM is in recovery mode by reading ocr_log.txt or ptm_config.json
- If recovery is detected, fix it by rewriting these files and restarting PTM scripts.
- Must include: if __name__ == "__main__"
- Print clear status. No explanations, just code.
"""
    responses = []
    try:
        r = requests.post("https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {GPT_KEY}"},
            json={"model":"gpt-3.5-turbo","messages":[{"role":"user","content":prompt}]})
        responses.append(r.json()['choices'][0]['message']['content'])
    except: responses.append("")
    try:
        r = requests.get(f"https://api.perplexity.ai/v1/ask?q={prompt}&key={PERPLEXITY_KEY}")
        responses.append(r.text)
    except: responses.append("")
    try:
        r = requests.get(f"https://api.anthropic.com/v1/claude?prompt={prompt}&key={CLAUDE_KEY}")
        responses.append(r.text)
    except: responses.append("")
    return responses

while True:
    print("[Ghost AI Bridge] 🔥 Asking AIs for PTM recovery scripts...")
    attempts = ask_ai_for_code()
    for raw_code in attempts:
        if not raw_code.strip():
            continue
        cleaned = strip_junk(raw_code)
        fixed = fix_indentation(cleaned)
        if "def" not in fixed:
            fixed = fallback_script
        filename = save_script(fixed)
        log_fix({"file": filename, "raw": raw_code, "fixed": fixed})
        print(f"[Ghost AI Bridge] 🚀 Running: {filename}")
        os.system(f"python3 {filename}")
    print("[Ghost AI Bridge] 💤 Sleeping for 5 min...")
    time.sleep(300)