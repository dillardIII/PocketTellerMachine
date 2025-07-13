#!/usr/bin/env python3
# === ghost_autonomy_integrator.py ===
# 🧬 Ensures each Ghost has full autonomy by pulling missing files.

import os
import shutil

AUTONOMY_LIB = "autonomy_lib"
LOCAL_DIR = "."

def integrate_autonomy():
    files = os.listdir(AUTONOMY_LIB)
    for f in files:
        local_path = os.path.join(LOCAL_DIR, f)
        if not os.path.exists(local_path):
            src_path = os.path.join(AUTONOMY_LIB, f)
            shutil.copy2(src_path, local_path)
            print(f"[Integrator] ⚙️ Integrated missing {f}")
    print("[Integrator] ✅ All autonomy modules active.")

if __name__ == "__main__":
    integrate_autonomy()