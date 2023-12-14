# zaimportuj biblioteke requests i BeautifulSoup do pythona
# pobierz strone 'https://archiwum.mz.gov.pl/zdrowie-i-profilaktyka/grypa/materialy-do-pobrania/'
# wyciagnij wszystkie elementy 'a' z linkiem do pliku '.pdf' tej strony
# pobierz plik 'pdf' na swoj komputer
import re

import requests
from bs4 import BeautifulSoup

# Pobierz stronę internetową
response = requests.get("https://archiwum.mz.gov.pl/zdrowie-i-profilaktyka/grypa/materialy-do-pobrania/")

# Utwórz obiekt BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Znajdź wszystkie linki do plików PDF
links = soup.find_all("a", {"href": re.compile(".*.pdf")})

# Pobierz wszystkie pliki PDF
for link in links:
    # Pobierz plik PDF
    response = requests.get(link["href"])
    # Zapisz plik PDF
    filename = link["href"].split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)