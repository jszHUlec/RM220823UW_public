import requests
from bs4 import BeautifulSoup

payload = {"Email":"aa@aa.com", "Password":"aaaa"}
url = "https://hack-yourself-first.com/Account/login"
result = requests.post(url, data=payload)

print(result.status_code)
print(result.text)

if "Log off" in result.text:
    print("Success")
else:
    print("blad")

parsed_r = BeautifulSoup(result.text, 'html.parser')

for a in parsed_r.find_all('a'):
    if "login" in a.text:
        requests.post()


