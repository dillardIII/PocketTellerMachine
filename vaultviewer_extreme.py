# === FILE: vaultviewer_extreme.py ===
print("[VaultViewer] 🎥 Showing vault contents:")
try:
    with open("4TB_WD/vault_private_keys.txt", "r") as f:
        keys = f.readlines()
        print(f"[VaultViewer] 🔑 Found {len(keys)} private keys.")
except:
    print("[VaultViewer] 🗃️ No private keys found yet.")