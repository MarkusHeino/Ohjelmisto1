import random

def roll_die(num_faces):
    return random.randint(1, num_faces)

num_faces = int(input("Anna nopan tahkojen lukumäärä: "))

if num_faces < 2:
    print("Nopallahan pitää olla yli kaksi tahkoa. Muuten se ei ole noppa, vaan kortti. DUH!")
else:
    max_value = num_faces
    while True:
        roll = roll_die(num_faces)

        print(f"Heitit {roll}")

        if roll == max_value:
            break
