# Napisz funkcje, ktora pobiera od uzytkownika wartosc (input)
# i dodaje 'ish' na koniec tej wartosci
# ---------------------- dodatkowy element ------------
# w funkcji pobieraj od uzytkownika tekst
# dopoki nie wpisze 'koniec'
# (czyli jesli 'koniec' to wyjdz z funkcji)

def Add(newword):
    print(newword+'ish')

while 1 == 1:
    word = input("Create New Word: ")
    if word == "End":
        break
    else:
        Add(word)


