import random

unit = int(input("Saisiko olla kolmen vai neljän numeron koodi?"))

a = (random.randint(0, 9))
b = (random.randint(0, 9))
c = (random.randint(0, 9))

d = (random.randint(1, 6))
e = (random.randint(1, 6))
f = (random.randint(1, 6))
g = (random.randint(1, 6))

if unit == 3:
    print(a, b, c)

elif unit == 4:
    print(d, e, f, g)

else:
    print("Pahoittelut, anna komennoksi joko 3 tai 4!")
