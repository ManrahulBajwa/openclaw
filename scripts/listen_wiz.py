import socket
import json

def listen_for_wiz():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(5.0)
    
    # Send registration/discovery to broadcast
    msg = '{"method":"getSystemConfig","params":{}}'
    sock.sendto(msg.encode(), ('255.255.255.255', 38899))
    
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")
    except socket.timeout:
        print("Done listening.")
    finally:
        sock.close()

if __name__ == "__main__":
    listen_for_wiz()
