
import socket
mysocket = socket.socket()
mysocket.bind(("0.0.0.0", 4444))
mysocket.listen(1)
conn, addr = mysocket.accept()

while True:
    data = conn.recv(2048).decode()
    data = data.replace("\n", "")
    print(f"odebrane: {data}")

    if data == "exit":
        break

    od_uzytkownika = input("wyslij: ")
    conn.send(od_uzytkownika.encode())

    if od_uzytkownika == "exit":
        break

mysocket.close()
print("koniec")