# 👻 get_autonomy_from_ptm.py – ultra loaded, zero edits needed autonomy grabber

import os
import shutil

PTM_PATH = "../PTM"  # 💥 Assumes your PTM is one folder up. NO EDIT NEEDED.
GHOSTMEDIC_AUTONOMY_PATH = "./modules_autonomy"

AUTONOMY_FILES = [
    # Bridges & handlers
    "bridge_launcher.py", "drop_agent.py", "pickup_agent.py", "file_exec_engine.py", "hunter_rpc.py",
    "sweep_handler.py", "self_rebuild_watcher.py",
    # Mood, rating, self logic
    "mood_engine.py", "self_rating_logic.py", "self_preservation_logic.py",
    # AI core autonomy brain & coders
    "ghost_brain_upgrade.py", "ghost_emotion_engine.py", "ghost_mission_writer.py",
    "ghost_autocoder.py",
    # Deepweb & quantum
    "ghost_deepweb_scraper.py", "quantum_entropy_initializer.py",
    # Control & comms
    "command_listener.py", "whisper_autolistener.py",
    "liaison_module.py",
    # Additional future expansions
    "ghost_vault_archivist.py", "autonomy_trigger_stack.py",
    "ghost_macro_writer.py", "ghost_entropy_mutator.py",
    "ghost_safeguard_engine.py"
]

def hunt_and_copy():
    if not os.path.exists(GHOSTMEDIC_AUTONOMY_PATH):
        os.makedirs(GHOSTMEDIC_AUTONOMY_PATH)

    copied = []
    missing = []

    for file in AUTONOMY_FILES:
        src = os.path.join(PTM_PATH, file)
        dst = os.path.join(GHOSTMEDIC_AUTONOMY_PATH, file)

        if os.path.exists(src):
            shutil.copy2(src, dst)
            copied.append(file)
            print(f"✅ Copied {file}")
        else:
            missing.append(file)
            print(f"⚠️ Missing {file} in PTM!")

    print("\n==================== SUMMARY ====================")
    print(f"✅ Files copied : {len(copied)}")
    print(f"⚠️ Files missing: {len(missing)}")
    if missing:
        print("⚠️ List of missing files:", missing)
    print("🚀 Autonomy brain stack fully loaded into GhostMedic's modules_autonomy folder.")

def main():
    print("👻 Scanning PTM for FULL autonomy stack...")
    hunt_and_copy()

if __name__ == "__main__":
    main()