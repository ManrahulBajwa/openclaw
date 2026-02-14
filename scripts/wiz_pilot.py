import socket
import json
import time

ip = "192.168.1.2"
port = 38899

def send(method, params):
    cmd = {"method": method, "params": params}
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(json.dumps(cmd).encode(), (ip, port))
    sock.close()

print("Trying setPilot...")
send("setPilot", {"state": False})
time.sleep(1)
send("setPilot", {"state": True})
print("Done.")
