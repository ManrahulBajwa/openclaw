import socket
import json
import sys

def send_wiz_command(ip, method, params=None):
    if params is None:
        params = {}
    cmd = {"method": method, "params": params}
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(json.dumps(cmd).encode(), (ip, 38899))
        sock.settimeout(2)
        data, addr = sock.recvfrom(1024)
        return json.loads(data.decode())
    except Exception as e:
        return {"error": str(e)}
    finally:
        sock.close()

if __name__ == "__main__":
    ip = "192.168.1.2"
    if len(sys.argv) < 2:
        print("Usage: python3 control_wiz.py [on|off|status|brightness <0-255>|color <r> <g> <b>]")
        sys.exit(1)
        
    action = sys.argv[1].lower()
    
    if action == "on":
        print(send_wiz_command(ip, "setState", {"state": True}))
    elif action == "off":
        print(send_wiz_command(ip, "setState", {"state": False}))
    elif action == "status":
        print(send_wiz_command(ip, "getPilot"))
    elif action == "brightness" and len(sys.argv) == 3:
        level = int(sys.argv[2])
        print(send_wiz_command(ip, "setState", {"dimming": level}))
    elif action == "color" and len(sys.argv) == 5:
        r, g, b = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        print(send_wiz_command(ip, "setState", {"r": r, "g": g, "b": b}))
    else:
        print("Invalid command or arguments.")
