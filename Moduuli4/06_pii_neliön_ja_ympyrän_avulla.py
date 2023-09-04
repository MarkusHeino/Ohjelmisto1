import random

pisteet = int(input("Anna pisteiden määrä väliltä 1000000-10000000:"))
osumat = 0

for i in range(pisteet):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y <1:
         osumat +=1
pi = 4* osumat / pisteet

print("Pii on", pi)