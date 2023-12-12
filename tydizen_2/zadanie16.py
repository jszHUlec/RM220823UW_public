# napisz trzy funkcje
# jedna funkcja przyjmuje od uzytkownika text
#   i zapisuje go w zmiennej global w formacie "data"+"wprowadzony text" ( import datetime # datetime.datetime.now() )
# druga funkcja
#     wysweitla zmienna globalna (wprowadzony tekst od uzytkownika + data)
#
# trzecia funkcja:
#     jest to menu do wyboru przez uzytkownika:
#         * 1. wprowadz
#         * 2. wyswietl
#         * 3. wyjdz
import datetime

tekst = []
def wprowadzanie():
    global tekst
    odUzytkownika = input("wpisz tekst:")
    data = datetime.datetime.now()
    #tekst = str(datetime.datetime.now()) + "\t" + tekst
    tekst.append(f"{data.year}.{data.month}.{data.day} {data.hour}:{data.minute}:{data.second} : {odUzytkownika}")


def wyswietlanie():
    for x in tekst:
        print(x)

def main():
    while True:
        print("1. wprowadź\n2. wyświetl\n3. wyjdź")
        wybor = input("")
        if wybor == "1":
            wprowadzanie()
        elif wybor == "2":
            wyswietlanie()
        elif wybor == "3":
            break
        else:
            print("Zły wybór!")

if __name__ == "__main__":
    main()
