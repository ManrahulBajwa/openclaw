import socket
import json
import time

ip = "192.168.1.2"
port = 38899

def send_and_receive(cmd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.0)
    try:
        sock.sendto(json.dumps(cmd).encode(), (ip, port))
        data, addr = sock.recvfrom(1024)
        return json.loads(data.decode())
    except Exception as e:
        return {"error": str(e)}
    finally:
        sock.close()

# Try to get status first
print("Status:", send_and_receive({"method": "getPilot", "params": {}}))

# Try a simple on/off
print("Turning OFF:", send_and_receive({"method": "setState", "params": {"state": False}}))
time.sleep(1)
print("Turning ON:", send_and_receive({"method": "setState", "params": {"state": True}}))
