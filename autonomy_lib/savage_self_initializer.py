# === FILE: savage_self_initializer.py ===
# 🚀 Self-initializes missing files & folders

import os

def create_dirs():
    for d in ["generated_ai_modules", "logs"]:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"[SelfInit] 🏗️ Created directory: {d}")

def create_json_placeholders():
    files = {
        "ptm_config.json": {"status": "stable", "recovery": False},
        "vault_status.json": {"vault": "healthy", "entropy_pools": 8, "shields": "active"},
        "liaison_status.json": {"liaison": "active"}
    }
    for file, data in files.items():
        if not os.path.exists(file):
            with open(file, 'w') as f:
                json.dump(data, f)
            print(f"[SelfInit] 📝 Created placeholder: {file}")

if __name__ == "__main__":
    print("[SelfInit] 🚀 Running savage self-initializer...")
    create_dirs()
    create_json_placeholders()