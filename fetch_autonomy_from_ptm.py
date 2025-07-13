# === FILE: fetch_autonomy_from_ptm.py ===
# 🚀 Savage GhostMedic Autonomy Fetcher
# Looks through your PTM repo & steals all core autonomy files into GhostMedic.

import os
import shutil

# === CONFIG ===
# Adjust to your PTM and GhostMedic locations
PTM_DIR = "/home/runner/ptm_workspace/modules_autonomy"
GHOSTMEDIC_DIR = "/home/runner/ghostmedic_workspace/modules_autonomy"

# List of critical autonomy files we need
REQUIRED_FILES = [
    'bridge_launcher.py', 'drop_agent.py', 'pickup_agent.py', 'file_exec_engine.py',
    'hunter_rpc.py', 'sweep_handler.py', 'self_rebuild_watcher.py', 'mood_engine.py',
    'self_rating_logic.py', 'self_preservation_logic.py', 'ghost_brain_upgrade.py',
    'ghost_emotion_engine.py', 'ghost_mission_writer.py', 'ghost_autocoder.py',
    'ghost_deepweb_scraper.py', 'quantum_entropy_initializer.py', 'command_listener.py',
    'whisper_autolistener.py', 'liaison_module.py', 'ghost_vault_archivist.py',
    'autonomy_trigger_stack.py', 'ghost_macro_writer.py', 'ghost_entropy_mutator.py',
    'ghost_safeguard_engine.py'
]

# === Create GhostMedic autonomy folder if needed ===
os.makedirs(GHOSTMEDIC_DIR, exist_ok=True)

# === Copy process ===
files_copied = 0
files_missing = []

print("\n👻 [GhostMedic Fetcher] Scanning PTM for autonomy files...")

for file_name in REQUIRED_FILES:
    ptm_path = os.path.join(PTM_DIR, file_name)
    dest_path = os.path.join(GHOSTMEDIC_DIR, file_name)
    if os.path.isfile(ptm_path):
        shutil.copy2(ptm_path, dest_path)
        print(f"✅ Copied: {file_name}")
        files_copied += 1
    else:
        print(f"⚠️ Missing in PTM: {file_name}")
        files_missing.append(file_name)

# === Summary ===
print("\n================== SUMMARY ==================")
print(f"🚀 Files copied: {files_copied}")
print(f"❌ Files still missing: {len(files_missing)}")
if files_missing:
    print("📝 Missing files list:")
    for f in files_missing:
        print(f"  - {f}")

print("\n[GhostMedic Fetcher] Completed savage scavenging run.\n")