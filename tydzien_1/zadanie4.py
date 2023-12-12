
# Pobierz od uzytkownika dwie liczby (oddzielone enterem)
# porownaj obie liczby
# napisz ktora liczba jest wieksza


num1 = int(input("Podaj pierwsza liczbe: "))
num2 = int(input("Podaj druga liczbe: "))

if num1 > num2:
    print(num1,"jest wieksze niz",num2)
elif num1 < num2:
    print(num2,"jest wieksze niz",num1)
else:
    print(num1,"jest rowna",num2)
