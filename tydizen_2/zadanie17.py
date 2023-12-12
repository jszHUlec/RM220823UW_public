import random

gr = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "10":0,
}

for x in range(1,100):
    zmienna = str(random.randint(1,10)) #str()
    gr[zmienna] = gr[zmienna]+1

print(gr)
# 99