# === FILE: main.py ===
# 🚀 PTM Launcher
import os

print("[Main] 🚀 Launching ghost brain...")

os.system("python3 ghost_brain.py")

print("[Main] ✅ Ghost brain running. Now triggering autonomy and vault...")

os.system("python3 autonomy_trigger_stack.py")
os.system("python3 vault_manager.py")

# Keep GhostMedic always running
while True:
    os.system("python3 ghostmedic.py")