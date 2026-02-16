import socket
import json

ips = ["192.168.1.7", "192.168.1.12", "192.168.1.9", "192.168.1.5", "192.168.1.13", "192.168.1.10", "192.168.1.6", "192.168.1.18", "192.168.1.4"]

def check_ip(ip):
    msg = {"method": "getPilot", "params": {}}
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.5)
    try:
        sock.sendto(json.dumps(msg).encode(), (ip, 38899))
        data, addr = sock.recvfrom(1024)
        return True
    except:
        return False
    finally:
        sock.close()

for ip in ips:
    if check_ip(ip):
        print(f"WiZ found at {ip}")
