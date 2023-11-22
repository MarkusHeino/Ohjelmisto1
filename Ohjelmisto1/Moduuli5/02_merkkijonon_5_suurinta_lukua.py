number = 0
numbers = []

while True:
    user_input = input("Anna vähintään viisi numeroa (ja sitten paina Enteriä): ")

    if user_input == "":
        break

    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Anna järkevä arvo.")

if len(numbers) >= 5:

    numbers.sort(reverse=True)

    largest_numbers = numbers[0: 5]

    print("Viisi suurinta numeroa laskevassa järjestyksessä:")
    for num in largest_numbers:
        print(num)
else:
    print("Anna vähintään viisi numeroa, jotta voin järjestää niistä viisi suurinta laskevaan järjestykseen.")