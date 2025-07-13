# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_reflex_integrator.py ===
# 🔥 Savage Reflex Integrator w/ live mutation + cross-bot patching

import os
import json
import time
import random
from datetime import datetime

QUANTUM_SHARDS = "quantum_shards.json"
SYNC_MESH = "sync_mesh.json"
MACRO_QUEUE = "macro_queue.json"
VAULT = "vault_status.json"

def load_json_safe(filepath, default):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return default

def mutate_code_logic(hint):
    """ Generates savage code based on mutation hint """
    if "risk" in hint:
        return "print('⚠️ High risk mode activated.')"
    elif "recursion" in hint:
        return "def recurse(n):\n    if n > 0:\n        print(f'Recursing: {n}')\n        recurse(n-1)\nrecurse(5)"
    elif "amplify" in hint:
        return "for i in range(10): print('🔥 Amplifying savage empire...')"
    else:
        return "print('👻 Savage mutation running.')"

def patch_file(filename, content):
    with open(filename, "w") as f:
        f.write(f"# 🧬 Savage Reflex Patch - {datetime.utcnow().isoformat()}\n")
        f.write(content)
    print(f"[Reflex] 🔥 Patched {filename}")

def main():
    print("[ReflexIntegrator] 🚀 Starting Savage Reflex Loop...")
    while True:
        shards = load_json_safe(QUANTUM_SHARDS, [])
        mesh = load_json_safe(SYNC_MESH, [])
        macros = load_json_safe(MACRO_QUEUE, [])

        mutation_hint = "neutral"
        if shards:
            shard = random.choice(shards)
            mutation_hint = shard.get("mutation_hint", "neutral")

        # Decide what to mutate
        target_file = random.choice([
            "ghostmedic.py", "ghost_programmer.py", 
            "bridge_launcher.py", "savage_macro_orchestrator.py"
        ])
        logic = mutate_code_logic(mutation_hint)
        patch_file(target_file, logic)

        # Log to vault
        vault_data = load_json_safe(VAULT, {})
        vault_data[f"mutation_{int(time.time())}"] = {
            "file": target_file,
            "hint": mutation_hint,
            "logic": logic
        }
        with open(VAULT, "w") as f:
            json.dump(vault_data, f, indent=2)
        print(f"[Reflex] 🧬 Updated vault with mutation record for {target_file}")

        time.sleep(8)  # spread mutations out

if __name__ == "__main__":
    main()