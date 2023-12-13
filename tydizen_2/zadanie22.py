import os

#zmodyfikuj zadanie aby pobrac IP zpliku 'nasze_ip.txt'
# w petli sprawdz IP wykorzystujac komende 'ping'
# rezultat pinga przekieruj do pliku ping_<IP>.txt
#######################################################

import os
ips = open("nasze_ip.txt", "r")
for ip in ips:
    ip = ip.replace("\n", "") # skasowanie "ENTERA" na koncu lini
    print(f'|{ip}|')
    os.system(f"ping -c 2 {ip} > ping_{ip}.txt")
    pingfile = open(f"ping_{ip}.txt", "r")
    for line in pingfile:
        if "ms" in line:
            print("ping correct")
            break


