# zaimportuj biblitoteke reqeuests
#
# przygotuj 'payload' z danymi logowania email:'aa@aa.com', password 'aaaa'
# wykonaj metode post na adres https://hack-yourself-first.com/Account/Login
#
# wyswietl rezultat tego zapytania

import requests

payload = {"Email":"aa@aa.com", "Password":"aaaa"}
url = "https://hack-yourself-first.com/Account/login"
result = requests.post(url, data=payload)

print(result.status_code)

if "Log off" in result.text:
    print("Success")
else:
    print("blad")

