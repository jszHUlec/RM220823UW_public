# masz plik z loginami
#     kali
#     admin
#     test
#
# masz plik z IP:
#     127.0.0.1
#     8.8.8.8
#     wp.pl
#
# Odczytaj oba pliki i stworz komende
#     ssh <login>@<ip>
# dla wszystkich kombinacji z pliku
import os

# ssh kali@127.0.0.1
# ssh kali@wp.pl
# ssh admin@127.0.0.1
# ssh admin@wp.pl

#tak przygotowana komende wypisz do pliku: atak.txt

loginy = open("login.txt","r")
ip_do_sprawdzenia = open("nasze_ip.txt","r")

kombinacje = []

for user in loginy:
    user = user.replace("\n", "")
    ip_do_sprawdzenia.seek(0) #wazne, zeby wrocic na poczatek pliku przed odczytem
    for ip in ip_do_sprawdzenia:
        ip = ip.replace("\n", "")
        kombinacje.append(f"ssh {user}@{ip}\n")


with open("atak.txt","w") as plik_zapis:
    plik_zapis.write("!#/bin/bash\n")
    for linijka in kombinacje:
        plik_zapis.write(linijka)
        #os.system(linijka)









