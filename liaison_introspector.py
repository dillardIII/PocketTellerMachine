# === liaison_introspector.py ===
# 🕵️‍♂️ Savage Empire Liaison
# Audits current directory and writes inventory to JSON

import os
import json

inventory = []

for root, dirs, files in os.walk("."):
    for file in files:
        inventory.append(os.path.join(root, file))

with open("liaison_inventory.json", "w") as f:
    json.dump(inventory, f, indent=2)

print("[LiaisonIntrospector] 🔍 Inventory written to liaison_inventory.json")