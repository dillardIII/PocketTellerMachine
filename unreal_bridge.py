import socket, json, time

def start_bridge():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 5566))
    sock.listen(5)
    print("🎮 Unreal Engine Bridge listening on port 5566...")
    while True:
        conn, addr = sock.accept()
        data = conn.recv(4096).decode()
        if data:
            print(f"🎬 Unreal received: {data}")
            conn.send("✅ Acknowledged by GhostMedic".encode())
        conn.close()

if __name__ == "__main__":
    start_bridge()