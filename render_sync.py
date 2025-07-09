import os, time

REPO = "https://github.com/YOUR_USER/YOUR_REPO.git"

def push_to_render():
    os.system("git add .")
    os.system('git commit -m "🛠 Auto update from GhostMedic"')
    os.system("git push origin main")
    print("🚀 Repo pushed to Render.")

if __name__ == "__main__":
    while True:
        push_to_render()
        time.sleep(300)