# Nawiaz polaczenie SSH z komputerem zdalnym
# podaj login
# haslo
# i wykonaj na nim polecenie 'whoami'


#zmodyfikuj kod, aby pobieral uzytkownika i haslo z pliku.
# przetestuj polaczenie !

import paramiko

sshClient = paramiko.SSHClient()

sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
try:
    sshClient.connect("10.0.2.30", 22, "kali", "kali", timeout=1)
    stdin, stdout, stderr = sshClient.exec_command("asdfasdf")
    print("stdout:", stdout.read().decode())
    print("stderr:", stderr.read().decode())
except:
    pass
finally:
    sshClient.close()


