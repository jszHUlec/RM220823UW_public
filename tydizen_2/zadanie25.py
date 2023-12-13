import urllib3

http = urllib3.PoolManager()
r = http.request("GET","http://marylarodowicz.pl//")
print(f"the page status is {r.status}")
print("Contents:\n\n")
print(r.data.decode("uf-8"))