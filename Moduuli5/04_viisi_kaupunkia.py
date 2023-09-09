city_names = []

for i in range(5):
    city = input(f"Anna viiden kaupungin nimet yksi kerrallaan. {i + 1}: ")

    city_names.append(city)

if city_names:
    print("Kaupunkien nimet antojärjestyksessä:")

    for city in city_names:
        print(city)

