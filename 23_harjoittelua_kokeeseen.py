first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

average = (first_number + second_number + third_number) /3
print(f"The average of {first_number}, {second_number}, and {third_number} is: {average:.2f}")


rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))

area = rectangle_length * rectangle_width
print(f"The area of the rectangle is {rectangle_width} times {rectangle_length} so the area is: {area:.2f}square meters.")

import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)
print(f"The area of the circle is {radius} times pi so the area is: {area:.2f}")


number1 = int(input("Enter a non negative integer: "))


import math

def calculate_factorial(num):
    factorial = math.factorial(num)
    print(f"The factorial value of {num} is: {factorial}")

# Prompt the user to enter a non-negative integer
num = int(input("Enter a non-negative integer: "))

# Call the function with the user's input
calculate_factorial(num)


square_length = float(input("Enter the length of the square: "))
square_width = float(input("Enter the width of the square: "))

area = square_length * square_width
print(f"The area of the rectangle is {square_width} times {square_length} so the area is: {area:.2f}square meters.")

import math
def calculate_factorial():

    number1 = int(input("Enter a number and I'll calculate its factorial: "))

    print(f"The factorial of {number1} is {math.factorial(number1)}.")
