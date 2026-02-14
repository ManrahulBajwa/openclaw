import socket
import json

def discover_wiz():
    discovery_msg = '{"method":"getSystemConfig","params":{}}'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(2)
    
    found_devices = []
    try:
        sock.sendto(discovery_msg.encode(), ('255.255.255.255', 38899))
        while True:
            data, addr = sock.recvfrom(1024)
            found_devices.append({"ip": addr[0], "data": json.loads(data.decode())})
    except socket.timeout:
        pass
    finally:
        sock.close()
    return found_devices

if __name__ == "__main__":
    devices = discover_wiz()
    print(json.dumps(devices, indent=2))
