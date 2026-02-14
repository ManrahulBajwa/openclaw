import socket
import json

def discover():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(5)
    
    # WiZ discovery message
    msg = '{"method":"getSystemConfig","params":{}}'
    
    try:
        sock.sendto(msg.encode(), ('255.255.255.255', 38899))
        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Found: {addr[0]} -> {data.decode()}")
    except socket.timeout:
        print("Discovery finished.")
    finally:
        sock.close()

if __name__ == "__main__":
    discover()
