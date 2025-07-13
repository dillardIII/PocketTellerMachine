# === FILE: ptm_system_test.py ===
import os

PTM_PATH = "/home/runner/workspace"
expected_files = [
    "ghost_brain.py", "bridge_launcher.py", "drop_agent.py",
    "pickup_agent.py", "file_exec_engine.py", "hunter_rpc.py",
    "sweep_handler.py", "self_rebuild_watcher.py", "mood_engine.py",
    "self_rating_logic.py", "self_preservation_logic.py",
    "ghost_brain_upgrade.py", "ghost_emotion_engine.py",
    "ghost_mission_writer.py", "ghost_autocoder.py",
    "ghost_deepweb_scraper.py", "quantum_entropy_initializer.py",
    "command_listener.py", "whisper_autolistener.py"
]

print("🔍 PTM System Integrity Check:")
for f in expected_files:
    path = os.path.join(PTM_PATH, f)
    if os.path.exists(path):
        print(f"✅ {f} is present.")
    else:
        print(f"❌ {f} is missing.")