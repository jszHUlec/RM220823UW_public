# a - append (dodaj do pliku)
# w - write (zapis do pliku)
# r - read (odczyt pliku)
with open("przyklad.txt","a+") as myfile:
    myfile.write("\nJestem komunikatem z programu")
    myfile.seek(0) # czytanie pliku od poczatku
    print(myfile.read())
