# === FILE: savage_ai_inventory.py ===
import os, json
from datetime import datetime

ai_manifest = []
scan_paths = ["~/workspace", "/storage/emulated/0/pydroid3", "/data/data/com.termux/files/home", "/mnt/4TB_WD"]

def scan_dir(path):
    path = os.path.expanduser(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py") or "ai" in file.lower():
                ai_manifest.append({
                    "file": os.path.join(root, file),
                    "discovered": datetime.utcnow().isoformat()
                })

for path in scan_paths:
    scan_dir(path)

with open("ai_manifest.json", "w") as f:
    json.dump(ai_manifest, f, indent=2)
print(f"[AI Inventory] 🔥 Found {len(ai_manifest)} AI modules. Saved to ai_manifest.json.")