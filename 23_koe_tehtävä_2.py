import random

def greet():
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")
    return name

def roll_dice(num_dice, num_faces):
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_faces)
        total += roll
    return total

name = greet()

num_dice = int(input("How many dice do you want to throw? "))
num_faces = int(input("How many faces per die? "))

total_face_value = roll_dice(num_dice, num_faces)
print(f"Dice total: {total_face_value}")
