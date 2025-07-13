# === Adapted for ghostmedic ===
import http.client
import ssl
import threading
import json
import time
from datetime import datetime
from urllib.parse import urlparse

def dump_to_vault(data):
    entry = {"timestamp": datetime.utcnow().isoformat(), "data": data}
    try:
        with open("vault_mutation_log.json", "r") as f:
            vault = json.load(f)
    except:
        vault = []
    vault.append(entry)
    with open("vault_mutation_log.json", "w") as f:
        json.dump(vault, f, indent=2)
    print("[VaultDump] 💾 JSON dumped to vault_mutation_log.json")

def savage_https_request(method, url, payload=None):
    parsed = urlparse(url)
    conn = http.client.HTTPSConnection(parsed.netloc, context=ssl.create_default_context())

    headers = {"Content-Type": "application/json"}
    body = json.dumps(payload) if payload else None

    try:
        conn.request(method, parsed.path or "/", body, headers)
        res = conn.getresponse()
        data = res.read().decode()
        print(f"[HTTPS] {res.status} {method} {url}")

        try:
            json_data = json.loads(data)
            dump_to_vault(json_data)
        except:
            print("[HTTPS] ❌ Not JSON or failed parse.")

    except Exception as e:
        print(f"[HTTPS] ⚠️ Error: {e}")
    finally:
        conn.close()

threads = []
for _ in range(5):
    t = threading.Thread(target=savage_https_request, args=("GET", "https://postman-echo.com/get"))
    t.start()
    threads.append(t)
    time.sleep(0.2)

for _ in range(5):
    t = threading.Thread(target=savage_https_request, args=("POST", "https://postman-echo.com/post", {"ptm":"savage","mode":"https"}))
    t.start()
    threads.append(t)
    time.sleep(0.2)

for t in threads:
    t.join()

print("[Ghost AI Bridge] 👑 Savage HTTPS socket multi-thread run complete.")