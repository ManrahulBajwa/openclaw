import socket
import json
import time

ip = "192.168.1.2"
port = 38899

def send(state):
    cmd = {"method": "setState", "params": {"state": state}}
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(json.dumps(cmd).encode(), (ip, port))
    sock.close()

# Blink twice
for _ in range(2):
    send(False)
    time.sleep(0.5)
    send(True)
    time.sleep(0.5)
