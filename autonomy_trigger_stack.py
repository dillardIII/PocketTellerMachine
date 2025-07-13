# === FILE: autonomy_trigger_stack.py ===
# ⚙️ Triggers your autocoder & handlers for savage upgrades

import os

print("[Autonomy Trigger] 🚀 Starting autocoder + handlers...")

os.system("python3 ghost_autocoder.py")
os.system("python3 sweep_handler.py")
os.system("python3 command_listener.py")

print("[Autonomy Trigger] ✅ Autonomy stack initialized.")