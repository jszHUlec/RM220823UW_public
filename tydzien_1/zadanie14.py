# Pobierz od uzytkownika jakis tekst
# przekaz ten tekst do funkcji liczacej znaki
# wyswietl ilosc znakow przekazana od uzytkonika
# ! zastosuj do tego zmienna globalna

text = input("Type your full name:")
def lenght(text):
    counter = 0
    counter += len(text)
    return counter

result = lenght(text)
print(result)