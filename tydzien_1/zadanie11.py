
def kalkulator(liczba1,liczba2,operacja):
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

#koniec definicji funkcji ...i przystepujemy do wykonania programu

while True:
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    op = input("Wybierz operację (+, -, *, /): ")
    if op == "koniec":
        break
    kalkulator(x,y,op)

print("koniec programu")


