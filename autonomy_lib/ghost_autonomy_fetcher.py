# === FILE: ghost_autonomy_fetcher.py ===
import os
import shutil

PTM_DIR = "./PTM/"
GHOSTMEDIC_DIR = "./GhostMedic/"

autonomy_files = ["ReflexEngine.py", "SweepHandler.py", "CommandListener.py"]

for file in autonomy_files:
    src = os.path.join(PTM_DIR, file)
    dst = os.path.join(GHOSTMEDIC_DIR, file)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"[AutonomyFetcher] 🧬 Copied {file} from PTM to GhostMedic.")
    else:
        print(f"[AutonomyFetcher] ⚠️ Missing {file} in PTM!")

print("[AutonomyFetcher] ✅ PTM autonomy merged into GhostMedic.")