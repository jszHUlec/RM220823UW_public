# wybierz losowa liczbe
# zapisz ja do zmiennej globalnej
# napisz funkcje ktora pobiera od uzytkownika liczbe
# jezeli liczba == wysolowa liczba to zakoncz program
# jezeli liczba != wylosowana liczba to powiedz uzytkownikowi jak daleko jest od szczescia
# jezeli odleglosc do 10 to cieplo
# jezeli odleglosc do 20 to chlodno
# jezeli odleglosc do 30 to lodowato

# generujemy wartosc z zakresu (1,100)

import random

los = random.randint(1, 100)
count = 0
def pobierz():
    global count
    while True:
        liczba = int(input("liczba całkowita: "))
        count += 1
        roznica = abs(los - liczba) # |-3| = 3, |3| = 3 - wartosc bezwzgledna

        if liczba == los:
            print("Znalazłeś! \U0001F603")
            print("Liczba prób:",count)
            break
        if roznica <= 5:
            print("gorąco! \U0001F324")
        elif roznica <= 10:
            print("ciepło!")
        elif roznica <= 20:
            print("chłodno!")
        elif roznica <= 30:
            print("lodowato!")
        else:
            print("mróz! \U0001F366")

pobierz()