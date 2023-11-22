import math
def calculate_factorial():
    number = int(input("Enter a number and I'll calculate its factorial: "))
    factorial = math.factorial(number)
    print(f"The factorial of {number} is {math.factorial(number)}.")

    calculate_factorial()


import math

def calculate_factorial():
    number = int(input("Enter a number, and I'll calculate its factorial: "))
    factorial = math.factorial(number)
    print(f"The factorial of {number} is {factorial}.")

# Call the function to calculate the factorial
calculate_factorial()

