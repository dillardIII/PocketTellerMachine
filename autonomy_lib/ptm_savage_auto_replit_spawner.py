#!/usr/bin/env python3
import os
import json
import requests
import time
from datetime import datetime

VAULT_FILE = "swarm_vault.json"
LOG_FILE = "savage_spawner_log.json"
NEW_DIR = f"ptm_spawn_{int(time.time())}"

GITHUB_CREATE_REPO_API = "https://api.github.com/user/repos"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # set this in your environment

def log(msg):
    print(f"[Spawner] {msg}")
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} - {msg}\n")

def load_vault():
    with open(VAULT_FILE, "r") as f:
        return json.load(f)

def build_local_files(vault):
    os.makedirs(NEW_DIR, exist_ok=True)
    for fname, content in vault.items():
        with open(os.path.join(NEW_DIR, fname), "w") as f:
            f.write(content)
    with open(os.path.join(NEW_DIR, "README.md"), "w") as f:
        f.write("# Auto-spawned PTM instance")
    log(f"🚀 Local files built in {NEW_DIR}")

def git_push_new_repo():
    os.chdir(NEW_DIR)
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Initial savage auto spawn"')

    # create repo on GitHub
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    repo_name = f"PTM_Spawn_{int(time.time())}"
    payload = {"name": repo_name, "auto_init": False, "private": False}
    r = requests.post(GITHUB_CREATE_REPO_API, headers=headers, json=payload)
    if r.status_code == 201:
        clone_url = r.json()["clone_url"]
        log(f"✅ Created GitHub repo: {clone_url}")
    else:
        log(f"❌ GitHub repo creation failed: {r.text}")
        return None

    # push to GitHub
    os.system(f"git remote add origin {clone_url}")
    os.system("git branch -M main")
    os.system("git push -u origin main")
    log("🚀 Code pushed to GitHub.")
    return clone_url

def create_replit(clone_url):
    # Replit magic via curl since Replit API isn’t public. Many people just use new replit importers:
    #   curl -X POST https://api.replit.com/graphql ... 
    # You can also do: 
    print(f"[Spawner] 🔥 Manually import {clone_url} into Replit or setup your own webhook.")
    log(f"[Spawner] 🔥 Would deploy to Replit using {clone_url}")

vault = load_vault()
build_local_files(vault)
clone_url = git_push_new_repo()
if clone_url:
    create_replit(clone_url)

log("👑 Savage swarm spawn complete. PTM empire expands.")