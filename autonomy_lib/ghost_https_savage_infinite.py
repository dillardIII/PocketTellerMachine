import http.client
import ssl
import threading
import json
import time
import random
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

def savage_https(method, url, payload=None):
    try:
        u = urlparse(url)
        port = u.port if u.port else 443
        conn = http.client.HTTPSConnection(u.hostname, port, context=ssl.create_default_context())
        path = u.path or "/"
        if method == "GET":
            conn.request("GET", path)
        else:
            body = json.dumps(payload)
            headers = {"Content-Type": "application/json"}
            conn.request("POST", path, body, headers)
        res = conn.getresponse()
        body = res.read()
        print(f"[HTTPS] {res.status} {method} {url}")
        try:
            json_data = json.loads(body)
            dump_to_vault(json_data)
        except:
            print("[HTTPS] ❌ No JSON to dump.")
    except Exception as e:
        print(f"[HTTPS] ⚠️ Error: {e}")
        savage_raw_tcp(method, url, payload)

def savage_raw_tcp(method, url, payload=None):
    try:
        u = urlparse(url)
        port = u.port if u.port else 443
        sock = ssl.wrap_socket(ssl.SSLSocket())
        sock.connect((u.hostname, port))
        req = f"{method} {u.path or '/'} HTTP/1.1\r\nHost: {u.hostname}\r\nConnection: close\r\n\r\n"
        sock.send(req.encode())
        resp = sock.recv(4096)
        print(f"[TCP Fallback] 🥩 Raw TCP got {len(resp)} bytes")
    except Exception as e:
        print(f"[TCP Fallback] ⚠️ Error: {e}")
    finally:
        try: sock.close()
        except: pass

def savage_worker(method, url, payload=None):
    while True:
        savage_https(method, url, payload)
        time.sleep(random.uniform(0.5, 3.5)) # savage random throttle

threads = []
for i in range(3):
    t = threading.Thread(target=savage_worker, args=("GET", "https://postman-echo.com/get"))
    t.start()
    threads.append(t)
    time.sleep(0.2)

for i in range(3):
    t = threading.Thread(target=savage_worker, args=("POST", "https://postman-echo.com/post", {"ptm":"savage","mode":"infinite"}))
    t.start()
    threads.append(t)
    time.sleep(0.2)

for t in threads:
    t.join()