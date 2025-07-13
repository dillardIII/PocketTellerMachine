#!/usr/bin/env python3
# === liaison_autonomy_harvester.py ===
# 🕷️ Savage PTM Autonomy Finder - crawls PTM repo for all autonomy-related files

import os
import json

PTM_PATH = "ptm_clone"
OUTPUT_JSON = "liaison_autonomy_findings.json"

# Keywords that define an 'autonomy file'
KEYWORDS = [
    "autonomy", "brain", "drop", "pickup", "file_exec",
    "hunter", "sweep", "rebuild", "mood", "self_rating",
    "self_preservation", "ghost", "bridge"
]

def scan_file_for_keywords(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read()
            for keyword in KEYWORDS:
                if keyword in content:
                    return True
    except:
        pass
    return False

def harvest_autonomy_files():
    findings = []
    for root, dirs, files in os.walk(PTM_PATH):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                if scan_file_for_keywords(full_path):
                    with open(full_path, "r") as f:
                        preview = f.read(200)  # first 200 chars preview
                    findings.append({
                        "file": full_path,
                        "preview": preview
                    })
    return findings

def main():
    print("[LiaisonHarvester] 🕷️ Starting savage scan for autonomy files...")
    results = harvest_autonomy_files()
    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)
    print(f"[LiaisonHarvester] ✅ Found {len(results)} autonomy files.")
    print(f"[LiaisonHarvester] 🔥 Results written to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()