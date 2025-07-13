# === savage_macro_expander.py ===
import json
from datetime import datetime

macros = [
    "ghost_dashboard.py",
    "ghost_dashboard_data.py",
    "ghost_dashboard_updater.py",
    "ghost_autopilot_trigger.py",
    "ghost_macro_writer.py"
]

queue = []
for file in macros:
    queue.append({
        "task": "generate_or_repair_file",
        "filename": file,
        "priority": "high",
        "requested_at": datetime.utcnow().isoformat() + "Z",
        "details": f"Auto-create savage module: {file}"
    })

with open("macro_queue.json", "w") as f:
    json.dump(queue, f, indent=2)

print("🚀 Savage macro queue expanded.")