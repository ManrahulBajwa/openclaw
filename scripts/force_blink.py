import socket
import json
import time

ip = "192.168.1.2"
port = 38899

def send(cmd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(json.dumps(cmd).encode(), (ip, port))
    sock.close()

print("Sending commands...")
# Toggle off/on quickly
send({"method": "setState", "params": {"state": False}})
time.sleep(1)
send({"method": "setState", "params": {"state": True}})
time.sleep(1)
send({"method": "setState", "params": {"state": False}})
time.sleep(1)
send({"method": "setState", "params": {"state": True}})
print("Commands sent.")
