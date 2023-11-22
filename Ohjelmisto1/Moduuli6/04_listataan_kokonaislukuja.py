def calculate_sum(numbers):
    return sum(numbers)

while True:
    input_str = input("Listaa haluamasi määrä kokonaisulukuja pilkuilla eroteltuina: ")
    first_calculation = input("Haluatko että listan numeroista lasketaan summa? kyllä/ei ")
    if first_calculation.lower() != 'kyllä':
        break

    try:
        number_list = [int(num) for num in input_str.split(',')]

        total = calculate_sum(number_list)
        print(f"Listan lukujen summa on {total}")
        break
    except ValueError:
        print("Vääränlainen arvo. Yritä uudelleen!.")

