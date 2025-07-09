# === FILE: quantum_brain_link.py ===
# 🧠 Quantum Brain Link – loads all AIs into GhostMedic

import json
from datetime import datetime

try:
    with open("ai_manifest.json", "r") as f:
        ai_list = json.load(f)
except FileNotFoundError:
    print("[QuantumBrain] ❌ ai_manifest.json not found.")
    ai_list = []

quantum_brain = {"timestamp": datetime.utcnow().isoformat(), "ai_count": len(ai_list), "modules": ai_list}
with open("quantum_brain.json", "w") as f:
    json.dump(quantum_brain, f, indent=2)

print(f"[QuantumBrain] 🧠 Quantum brain online with {len(ai_list)} AIs.")