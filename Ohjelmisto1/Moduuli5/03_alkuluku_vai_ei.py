def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

user_input = input("Anna luku: ")

try:
    number = int(user_input)
    if is_prime(number):
        print(f"{number} on alkuluku.")
    else:
        print(f"{number} ei ole alkuluku.")
except ValueError:
    print("Väärä arvo. Yritä uuudelleen.")
