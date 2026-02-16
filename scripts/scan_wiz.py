import socket
import json
import threading

def check_ip(ip, found):
    msg = {"method": "getPilot", "params": {}}
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(0.5)
    try:
        sock.sendto(json.dumps(msg).encode(), (ip, 38899))
        data, addr = sock.recvfrom(1024)
        found.append(ip)
    except:
        pass
    finally:
        sock.close()

found = []
threads = []
for i in range(1, 255):
    ip = f"192.168.1.{i}"
    t = threading.Thread(target=check_ip, args=(ip, found))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(json.dumps(found))
