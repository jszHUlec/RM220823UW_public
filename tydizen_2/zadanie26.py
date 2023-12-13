import requests

req = requests.get("http://marylarodowicz.pl/pl")
print(req.status_code)
print(req.text)

with open("index.html","w") as plik:
    plik.write(req.text)