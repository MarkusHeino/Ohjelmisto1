def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

while True:
    input_str = input("Anna kokonaisulukuja pilkuilla eroteltuina: ")

    try:
        number_list = [int(num) for num in input_str.split(',')]

        filter_odd = input("Haluatko että tulostan listan ilman parittomia lukuja? (kyllä/ei): ")

        if filter_odd.lower() == 'kyllä':
            filtered_list = remove_odd_numbers(number_list)

            print("Ja tässä lista ilman parittomia lukuja:", filtered_list)
            print("Tässä alkuperäinen lista:", number_list)
            break
    except ValueError:
        print("Vääränlainen arvojono. Yritä uudelleen! Muista käyttää pilkkuja kokonaislukujen välissä.")

