import random

input("Saisiko olla kolmi- ja nelinumeroinen satunnaisesti generoitu koodisarja?")

print("Täältä pesee!")

fixed_digits = 3
print(random.randrange(000, 999, fixed_digits))

fixed_digits = 4
print(random.randrange(1111, 6666, fixed_digits))
