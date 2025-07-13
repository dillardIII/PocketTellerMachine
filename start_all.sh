#!/bin/bash
nohup python3 ghost_brain.py &
nohup python3 ghost_brain_upgrade.py &
nohup python3 ghost_emotion_engine.py &
nohup python3 ghost_mission_writer.py &
nohup python3 ghost_deepweb_scraper.py &
nohup python3 ghost_autocoder.py &
nohup python3 self_rebuild_watcher.py &
wait