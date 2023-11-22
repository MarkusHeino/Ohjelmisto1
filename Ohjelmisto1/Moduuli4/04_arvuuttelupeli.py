import random

n = random.randrange(1, 10)

arvaus = int(input("Anna luku: "))

while n != arvaus:

    if arvaus < n:
        print("Liian pieni arvaus.")
        arvaus = int(input("Enter number again: "))

    elif arvaus > n:
        print("Liian suuri arvaus.")
        arvaus = int(input("Enter number again: "))

    else:
        break

print("Oikea vastaus!")
