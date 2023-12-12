"""
zbuduj program, ktory pobiera od uzytkonika 4 marki pojazdu (petla z input) - done
uzupelnia tymi pojazdami liste (list.append()) - done
po wykonaniu pierwzej petli przechodzi do nastepnej
w ktorej pyta czy lista powinna byc wyswietlona
jesli odpowiedz 'tak' to wydrukuj liste w petli
"""


marki = []

for x in range(4):
    odUzytkownika = input("podaj marka")
    marki.append(odUzytkownika)

czy_wyswietlic = input("Lista uzupelniona. Czy wysweitlic liste?")
if czy_wyswietlic == "yes":
    print(marki)

print("koniec")
