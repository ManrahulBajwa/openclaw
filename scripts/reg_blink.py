import socket
import json

ip = "192.168.1.2"
my_ip = "192.168.1.66"
port = 38899

def send(cmd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.0)
    try:
        sock.sendto(json.dumps(cmd).encode(), (ip, port))
        data, addr = sock.recvfrom(1024)
        return data.decode()
    except Exception as e:
        return str(e)
    finally:
        sock.close()

# Register first
reg = {"method":"registration","params":{"phoneIp":my_ip,"register":True,"phoneMac":"c8d3ff993843"}}
print("Registration:", send(reg))

# Then try to blink
print("Blink Off:", send({"method":"setState","params":{"state":False}}))
import time
time.sleep(1)
print("Blink On:", send({"method":"setState","params":{"state":True}}))
