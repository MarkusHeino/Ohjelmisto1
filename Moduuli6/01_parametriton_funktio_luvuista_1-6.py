import random

def roll_die():
    return random.randint(1, 6)

while True:
    roll = roll_die()

    print(f"Heitit noppaa ja silmäluku on {roll}.")

    if roll == 6:
        break
