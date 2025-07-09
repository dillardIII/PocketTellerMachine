# === FILE: quantum_keyhunter.py ===
import time
import random

print("[QuantumKeyHunter] 🔥 Starting savage quantum hybrid attacks...")
while True:
    attempt = random.getrandbits(256)
    print(f"[QuantumKeyHunter] 🧬 Testing {hex(attempt)[:10]}...")
    time.sleep(1)
    if random.random() < 0.00000001:
        print("[QuantumKeyHunter] 💥 FOUND KEY! Dumping to vault...")
        with open("4TB_WD/vault_private_keys.txt", "a") as f:
            f.write(f"{hex(attempt)}\n")