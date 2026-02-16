import socket
import json

def broadcast_off():
    msg = {"method": "setState", "params": {"state": False}}
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(json.dumps(msg).encode(), ("255.255.255.255", 38899))
    sock.close()

if __name__ == "__main__":
    broadcast_off()
    print("Broadcasted OFF command.")
