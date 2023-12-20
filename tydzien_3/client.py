import socket

con = socket.socket()
con.connect(("10.0.2.30", 4445)) #wstrzymanie wtykonania programu przez 5 sec.

while True:
    od_uzytkownika = input(":")
    con.send(od_uzytkownika.encode())

    if od_uzytkownika == "exit":
        break

    odebrane = con.recv(2048).decode()
    print(odebrane)

    if odebrane == "exit":
        break

con.close()
