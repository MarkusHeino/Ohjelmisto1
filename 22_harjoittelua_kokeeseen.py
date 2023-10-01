import random

def greeting():
    name = input("Hei! Anna nimesi: ")
    print(f"Hei, {name}. Montako noppaa heitetään?")

def roll_dice(num_dice, num_faces):
    total = 0
    for in range(num_dice):
        roll = random.randint(1, num_faces)
        total += roll


what kind of printout does this python code give:

(red, blue) = (8, 5)
colours = (red, blue)
print(colours[1])
print(blue)
print(colours)

what kind of printout does this python code give:

p1 = "Miriam"
p2 = "Vesa"

if not p1 == p2:
    print("Alpha")
elif p2 == "Jani":
    print("Beta")
else:
    print("Charlie")
print("Delta")

