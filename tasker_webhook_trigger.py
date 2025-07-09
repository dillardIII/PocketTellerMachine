import requests, time

TASKER_URL = "http://192.168.1.X:8765"  # your Tasker HTTP Server

def notify_tasker():
    payload = {"event":"GhostMedicUpdate","msg":"All systems stable"}
    try:
        requests.post(TASKER_URL, json=payload)
        print("📱 Sent Tasker trigger.")
    except:
        print("❌ Tasker HTTP failed.")

if __name__ == "__main__":
    while True:
        notify_tasker()
        time.sleep(120)