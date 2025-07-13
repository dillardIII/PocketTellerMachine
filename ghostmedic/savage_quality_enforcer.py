# === Adapted for ghostmedic ===
# === FILE: savage_quality_enforcer.py ===
# 💎 Ensures all generated modules meet minimal length & format

import os

def enforce_quality():
    for root, dirs, files in os.walk("generated_ai_modules"):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                if len(content) < 20:
                    print(f"[QualityEnforcer] 🚨 {file} too short. Removing.")
                    os.remove(path)
                elif not content.strip().startswith("def"):
                    print(f"[QualityEnforcer] ⚠️ {file} doesn't start with def. Fixing.")
                    with open(path, 'w') as f:
                        f.write(f"def auto_patch():\n    print('Auto-patched {file}')\n")

if __name__ == "__main__":
    print("[QualityEnforcer] 💎 Running savage quality check...")
    enforce_quality()