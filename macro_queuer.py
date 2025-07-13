# === FILE: macro_queuer.py ===
# ⚙️ Builds macro tasks to auto-fix, generate, or upgrade missing files based on liaison_master output

import json
import os
from datetime import datetime

LIAISON_LOG = "global_ai_inventory.json"
MACRO_QUEUE = "macro_queue.json"

def load_liaison_log():
    if not os.path.exists(LIAISON_LOG):
        print(f"🚨 No liaison log found at {LIAISON_LOG}")
        return None
    with open(LIAISON_LOG, "r") as f:
        return json.load(f)

def build_macro_tasks(missing_files):
    tasks = []
    for file in missing_files:
        tasks.append({
            "task": "generate_or_repair_file",
            "filename": file,
            "priority": "high",
            "requested_at": datetime.utcnow().isoformat() + "Z",
            "details": f"Auto-create or repair missing critical autonomy file: {file}"
        })
    return tasks

def save_macro_queue(tasks):
    if os.path.exists(MACRO_QUEUE):
        with open(MACRO_QUEUE, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.extend(tasks)
    with open(MACRO_QUEUE, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"✅ Saved {len(tasks)} new macro tasks to {MACRO_QUEUE}")

def main():
    liaison_data = load_liaison_log()
    if not liaison_data:
        return

    missing_files = liaison_data.get("missing_files", [])
    if not missing_files:
        print("🎉 No missing critical files detected. System is fully stocked.")
        return

    tasks = build_macro_tasks(missing_files)
    save_macro_queue(tasks)
    print("🚀 Macro queue updated and ready for GhostMedic or GhostProgrammer to process.")

if __name__ == "__main__":
    main()