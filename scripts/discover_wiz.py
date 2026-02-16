import socket
import json

def discover_wiz():
    msg = {"method": "getPilot", "params": {}}
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(2)
    
    # Send broadcast
    sock.sendto(json.dumps(msg).encode(), ("255.255.255.255", 38899))
    
    found = []
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            found.append((addr[0], json.loads(data.decode())))
    except socket.timeout:
        pass
    finally:
        sock.close()
    return found

if __name__ == "__main__":
    devices = discover_wiz()
    if not devices:
        print("No WiZ devices found.")
    for ip, info in devices:
        print(f"Found: {ip} - {info}")
