num1 = 10
num2 = 0

try:
    print(num1/num2) # generuje blad
    print("koniec try")
except FileNotFoundError as e:
     print("obsluga bledu dzielenia przez zero: ") # w tym kawalku jest on obslugiwany
     # print(e.__traceback__)


print("koniec programu")