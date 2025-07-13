# === Adapted for ghostmedic ===

def fix_ptm():
    print("🛠 Forcing PTM out of recovery mode...")
    with open("ocr_log.txt", "w") as f:
        f.write("PTM STATUS: OK")
    with open("ptm_config.json", "w") as f:
        f.write('{"status":"stable","recovery":false}')
    print("✅ PTM forced stable.")
fix_ptm()
