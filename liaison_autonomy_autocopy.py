#!/usr/bin/env python3
# === liaison_autonomy_autocopy.py ===
# 🔥 Copies autonomy files from PTM clone into autonomy_lib/

import os
import shutil
import json

PTM_CLONE_DIR = "ptm_clone"
AUTONOMY_DIR = "autonomy_lib"
FINDINGS_FILE = "liaison_autonomy_findings.json"

def load_findings():
    try:
        with open(FINDINGS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[AutoCopy] ⚠️ Failed loading findings: {e}")
        return []

def ensure_autonomy_dir():
    if not os.path.exists(AUTONOMY_DIR):
        os.makedirs(AUTONOMY_DIR)
        print(f"[AutoCopy] 📂 Created {AUTONOMY_DIR} directory.")

def extract_path(item):
    if isinstance(item, dict):
        return item.get("path") or item.get("file") or list(item.values())[0]
    return item

def copy_files(files):
    for file_entry in files:
        file_path = extract_path(file_entry)
        if not isinstance(file_path, str):
            print(f"[AutoCopy] ⚠️ Skipping invalid entry: {file_entry}")
            continue
        src = os.path.join(PTM_CLONE_DIR, file_path)
        dst = os.path.join(AUTONOMY_DIR, os.path.basename(file_path))
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"[AutoCopy] ✅ Copied {file_path} to {AUTONOMY_DIR}/")
        else:
            print(f"[AutoCopy] ⚠️ Source missing: {file_path}")

def main():
    print("[AutoCopy] 🔥 Starting autonomy file copy process...")
    ensure_autonomy_dir()
    findings = load_findings()
    copy_files(findings)
    print("[AutoCopy] 🚀 All autonomy files now in autonomy_lib/ for GhostMedic.")

if __name__ == "__main__":
    main()