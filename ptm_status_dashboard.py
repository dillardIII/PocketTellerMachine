#!/usr/bin/env python3
"""
PTM Status Dashboard
- Scans all known PTM status files
- Reports if in recovery or stable
- Lists last few lines of key logs
"""

import os
import json

def read_status_file(path):
    if not os.path.exists(path):
        return f"{path}: ❌ Missing"
    with open(path, "r") as f:
        try:
            content = f.read()
            if path.endswith(".json"):
                parsed = json.loads(content)
                return f"{path}: ✅ JSON loaded - {parsed}"
            else:
                return f"{path}: ✅ Text loaded - {content.strip()[:80]}"
        except Exception as e:
            return f"{path}: ⚠️ Error loading - {e}"

status_files = [
    "ocr_log.txt",
    "ptm_config.json",
    "mutation_log.json",
    "mutation_research_log.json",
    "liaison_status.json",
    "vault_status.json"
]

print("🔍 PTM STATUS DASHBOARD ==========================")
for file in status_files:
    print(read_status_file(file))
print("=================================================")