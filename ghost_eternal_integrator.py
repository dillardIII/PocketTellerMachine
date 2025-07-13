#!/usr/bin/env python3
# === ghost_eternal_integrator.py ===
# 🔥 Reloads all autonomy modules.

import os
import subprocess

def reload_autonomy():
    files = os.listdir("autonomy_lib")
    for file in files:
        if file.endswith(".py"):
            path = os.path.join("autonomy_lib", file)
            print(f"[Integrator] 🚀 Running {path}")
            subprocess.run(["python3", path])

def main():
    print("[Integrator] 🔥 Reloading GhostMedic with merged autonomy...")
    reload_autonomy()
    print("[Integrator] ✅ Savage reload complete.")

if __name__ == "__main__":
    main()