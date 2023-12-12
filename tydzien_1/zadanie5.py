# pobierz dwie wartosci numeryczne od uzytkownika
# stworzy konstrukcje if/elif aby wykonac podstawowe operacje artmetyczne
# + - / *
# zaprezentuj wynika na ekranie

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

operacja = input("Wybierz operację (+, -, *, /): ")

if operacja == "+":
    wynik = liczba1 + liczba2
    print(f"Wynik dodawania: {wynik}")
elif operacja == "-":
    wynik = liczba1 - liczba2
    print(f"Wynik odejmowania: {wynik}")
elif operacja == "*":
    wynik = liczba1 * liczba2
    print(f"Wynik mnożenia: {wynik}")
elif operacja == "/":

    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print(f"Wynik dzielenia: {wynik}")
    else:
        print("Dzielenie przez zero jest niemożliwe.")
else:
    print("Błędna operacja. Wybierz spośród: +, -, *, /")