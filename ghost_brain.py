# === FILE: ghost_brain.py ===
# 🧠 Ghost Brain - Core savage intelligence for PTM empire

import time

from bridge_launcher import start_bridge
from drop_agent import DropAgent
from pickup_agent import PickupAgent
from file_exec_engine import FileExecEngine
from hunter_rpc import HunterRPC
from sweep_handler import SweepHandler
from self_rebuild_watcher import SelfRebuildWatcher
from mood_engine import MoodEngine
from self_rating_logic import SelfRating
from self_preservation_logic import SelfPreservation
from ghost_brain_upgrade import BrainUpgrade
from ghost_emotion_engine import EmotionEngine
from ghost_mission_writer import MissionWriter
from ghost_autocoder import GhostAutocoder
from ghost_deepweb_scraper import DeepWebScraper
from quantum_entropy_initializer import QuantumEntropy
from command_listener import CommandListener
from whisper_autolistener import WhisperListener

print("[GhostBrain] 🚀 Booting savage ghost brain...")

# === Initialize modules ===
start_bridge()
drop = DropAgent()
pickup = PickupAgent()
exec_engine = FileExecEngine()
rpc = HunterRPC()
sweeper = SweepHandler()
watcher = SelfRebuildWatcher()
mood = MoodEngine()
rating = SelfRating()
preserve = SelfPreservation()
upgrade = BrainUpgrade()
emotion = EmotionEngine()
mission = MissionWriter()
autocoder = GhostAutocoder()
scraper = DeepWebScraper()
entropy = QuantumEntropy()
listener = CommandListener()
whisper = WhisperListener()

print("[GhostBrain] ✅ All modules initialized.")

# === Main savage intelligence loop ===
while True:
    drop.run()
    pickup.run()
    exec_engine.run()
    rpc.run()
    sweeper.run()
    watcher.run()
    mood.process()
    rating.evaluate()
    preserve.secure()
    upgrade.evolve()
    emotion.react()
    mission.plan()
    autocoder.auto_write()
    scraper.scrape()
    entropy.inject()
    listener.listen()
    whisper.listen()
    time.sleep(0.2)