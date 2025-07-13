# === ghost_start_all.py ===
# 🚀 Savage Empire All-Systems Launcher
# Launches GhostMedic, GhostProgrammer, RepoSyncer, Liaison together

import threading
import time
import os

def run_ghostmedic():
    print("[Launcher] 🩺 Starting GhostMedic...")
    os.system("python3 ghostmedic.py")

def run_ghostprogrammer():
    print("[Launcher] 🤖 Starting GhostProgrammer...")
    os.system("python3 ghost_programmer.py")

def run_ghostreposyncer():
    print("[Launcher] 🔄 Starting GhostRepoSyncer...")
    os.system("python3 ghost_repo_syncer.py")

def run_liaison():
    print("[Launcher] 🕵️‍♂️ Starting LiaisonIntrospector...")
    os.system("python3 liaison_introspector.py")

threads = []
threads.append(threading.Thread(target=run_ghostmedic))
threads.append(threading.Thread(target=run_ghostprogrammer))
threads.append(threading.Thread(target=run_ghostreposyncer))
threads.append(threading.Thread(target=run_liaison))

for t in threads:
    t.start()
    time.sleep(2)

for t in threads:
    t.join()

print("[Launcher] 🚀 All systems live. Savage Empire operational.")