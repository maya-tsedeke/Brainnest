import socket

host = 'example.com'
port_list = [53, 80, 8080, 443]
for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        print(f"Port {port} is open")
    except Exception as e:
        print(f"Port {port} is closed ({e})")
    finally:
        s.close()
