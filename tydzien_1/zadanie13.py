


# Napisz program, ktory czyta login i password od uzytkownika - OK
# i sprawdza czy taki login i haslo sa zapisane w naszym slowniku
# realizacja jako funkcja
# jezeli wartosci bledne, to powtarzamy
# jezeli wartosci OK, to komunikat o sukcesie.
bazadanych = {"login":"admin", "password":"qwerty"}
def logowanie():

    while True:
        login = input("Podaj login: ")
        haslo = input("Podaj haslo: ")

        if login == bazadanych["login"] and haslo == bazadanych["password"]:
            print("Sukces! Zalogowano.")
            break
        else:
            print("Błędny login lub hasło. Spróbuj ponownie.")


logowanie()






