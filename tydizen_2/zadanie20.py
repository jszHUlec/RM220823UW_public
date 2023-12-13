# pobierz od uzytkownika dwie wartosci
# druga powinna byc '0'
# wykonaj dzielenie na tych wartosciach
# i przy dzieleniu przez zero pokaz komunikat 'probujesz dzilic przez 0'
import traceback
var1 = ""
var2 = ""
def collect():
    global var1
    global var2
    var1 = input("Type in the first number: ")
    var2 = input("Type in the second number: ")

def division():
    try:
        num1 = float(var1)
        num2 = float(var2)
        result = num1 / num2
        print(f"Division result: {round(result,2)}")
    except ZeroDivisionError as e:
        print("Division by zero is forbidden!")
        print(traceback.format_exc())
def main():
    print("To make a divison, type your numbers")
    while True:
        collect()
        division()

if __name__ == "__main__":
    main()