# zaimportuj biblioteke requests i BeautifulSoup do pythona
# pobierz strone 'https://hackthissite.org'
# wyciagnij wszystkie elementy 'a' z tej strony
#
# jezeli elementy 'a' zawieraja '.js' to je wyswietl

# z elementu 'a' wyciagnac 'href' zmienna.get('href')


import requests
from bs4 import BeautifulSoup

url = "https://hackthissite.org"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
tag = "script"
parameter = "src"

try:
    for el in soup.find_all(tag):
        print(el)
        s = el.get(parameter)
        if ".js" in s:
            print(requests.get(s).text)
except:
    print("nie wszystkie elementy udalo sie przetworzyc")