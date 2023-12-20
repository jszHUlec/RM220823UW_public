import socket
import time

mysocket = socket.socket()
mysocket.bind(("0.0.0.0", 4444))
mysocket.listen(1)
conn, adr = mysocket.accept()

time.sleep(10)
mysocket.close()
