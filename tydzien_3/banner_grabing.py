import socket
target = "10.0.2.30"
port = [80, 21]

while True:
    try:
        for port in port:
            sock = socket.socket()
            socket.setdefaulttimeout(4)
            sock.connect((target, int(port)))
            sock.send("what the service?\r\n".encode())
            ret = sock.recv(1024).decode()
            print(f"[+] the service: {ret} and port: {port}")
            sock.close()


        break
    except Exception as e:
        print(e)
        continue