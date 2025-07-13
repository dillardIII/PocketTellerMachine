# === FILE: hunt_for_autonomy_files.py ===
# 🚀 GhostMedic Directory Hunter - Find missing autonomy files anywhere in PTM

import os

# Adjust to your PTM root
PTM_ROOT_DIR = "/home/runner/ptm_workspace"

# What we want
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

found_files = {}

# Walk entire PTM tree
for root, dirs, files in os.walk(PTM_ROOT_DIR):
    for file in files:
        if file in REQUIRED_FILES:
            found_files[file] = os.path.join(root, file)

# Print results
print("\n=== 🕵️ GhostMedic Hunter Results ===")
if found_files:
    for f, path in found_files.items():
        print(f"✅ Found {f} at: {path}")
else:
    print("⚠️ No autonomy files found anywhere in PTM.")

missing_files = [f for f in REQUIRED_FILES if f not in found_files]
if missing_files:
    print("\n❌ Still missing these files:")
    for f in missing_files:
        print(f" - {f}")

print("\n[GhostMedic Hunter] Completed scan.\n")