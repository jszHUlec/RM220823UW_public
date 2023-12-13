# Mamy plik log.txt
#
# Odzytaj ten plik i sprawdz linijka po linijce
#     wyswietl w terminalu tylko linijki, ktore zawieraja 'ERROR'


with open("log.txt", "r") as logs:
    for log in logs:
        log = log.replace("\n", "")
        if "ERROR" in log:
            log_elements = log.split(" ")
            for i in range(4):
                print(f"{log_elements[i]}", end=" ")
            # print(f"{log_elements[0:4]}")
            print()

