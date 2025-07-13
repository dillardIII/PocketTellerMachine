# === Adapted for ghostmedic ===
#!/usr/bin/env python3
import socket
import ssl
import json
import time
from urllib.parse import urlparse
from threading import Thread
from datetime import datetime

def savage_http_request(method, url, payload=None, max_retries=5):
    retries = 0
    delay = 1

    while retries < max_retries:
        try:
            parsed = urlparse(url)
            host = parsed.hostname
            port = parsed.port or 443
            path = parsed.path or "/"

            # Build request
            request_line = f"{method} {path} HTTP/1.1\r\n"
            headers = f"Host: {host}\r\nConnection: close\r\n"
            body = ""
            if payload:
                body = json.dumps(payload)
                headers += "Content-Type: application/json\r\n"
                headers += f"Content-Length: {len(body)}\r\n"
            request_data = request_line + headers + "\r\n" + body

            # Connect socket
            sock = socket.create_connection((host, port))
            sock = ssl.wrap_socket(sock)
            sock.sendall(request_data.encode())

            response = b""
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                response += data
            sock.close()

            # Parse headers + body
            header_part, _, body_part = response.partition(b"\r\n\r\n")
            print("[Savage HTTPS] 🔥 Headers:\n", header_part.decode())
            print("[Savage HTTPS] 📦 Body:\n", body_part.decode())

            # Try JSON parse & vault dump
            try:
                json_body = json.loads(body_part)
                print("[Savage HTTPS] ✅ Parsed JSON:\n", json.dumps(json_body, indent=2))
                dump_to_vault(json_body)
            except:
                print("[Savage HTTPS] ❌ Not JSON body.")

            # Handle 301/302 redirect
            if b"301 Moved" in header_part or b"302 Found" in header_part:
                for line in header_part.split(b"\r\n"):
                    if line.lower().startswith(b"location:"):
                        new_url = line.split(b":", 1)[1].strip().decode()
                        print(f"[Savage HTTPS] 🚀 Following redirect to {new_url}")
                        url = new_url
                        retries = 0
                        delay = 1
                        break
                else:
                    break
            else:
                break  # success, exit loop

        except Exception as e:
            print(f"[Savage HTTPS] ⚠️ Error: {e}")
            retries += 1
            print(f"[Savage HTTPS] 🔄 Retrying in {delay} sec (attempt {retries}/{max_retries})")
            time.sleep(delay)
            delay *= 2

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

def savage_thread_worker(method, url, payload=None):
    savage_http_request(method, url, payload)

# MULTI-THREAD LAUNCHER
print("[Ghost AI Bridge] 🐍 Savage multi-thread HTTPS with vault JSON dump engaged...")

threads = []
for i in range(5):  # adjust thread count as savage as you like
    t = Thread(target=savage_thread_worker, args=("GET", "https://postman-echo.com/get"))
    t.start()
    threads.append(t)

for i in range(5):
    t = Thread(target=savage_thread_worker, args=("POST", "https://postman-echo.com/post", {"ptm":"savage","mode":"https"}))
    t.start()
    threads.append(t)

# Wait for all
for t in threads:
    t.join()

print("[Ghost AI Bridge] 👑 Savage multi-thread run complete. Vault logs updated.")