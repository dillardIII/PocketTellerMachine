# === FILE: savage_status_checker.py ===
# 📊 Prints simple PTM health readout

import json

def read_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return None

if __name__ == "__main__":
    print("[StatusChecker] 📊 Checking savage empire status...")

    for file in ["ptm_config.json", "vault_status.json", "liaison_status.json"]:
        data = read_json(file)
        if data:
            print(f"{file}: ✅ {data}")
        else:
            print(f"{file}: ❌ Missing or corrupted.")