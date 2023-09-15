import random

# luodaan uusi tietorakenne tallentamaan nimet
unique_names = set()

# luodaan lista, joka tallentaa nimien antojärjestyksen
input_order = []

# kysy käyttäjältä nimiä, kunnes tämä antaa tyhjän vastauksen
while True:
    name = input("Anna nimi tai sitten paina Enteriä lopettaaksesi: ")

    # jos käyttäjä haluaa lopettaa
    if name == "":
        break

    # tarkista onko nimi vanha vai uusi
    if name in unique_names:
        print(f"'{name}' on aiemman annettu nimi.")
    else:
        print(f"'{name}' on uusi nimi.")

    # lisätään listoihin uuden nimet ja antojärjestys
    unique_names.add(name)
    input_order.append(name)

# sekoitetaan niminen antojärjestys
random.shuffle(input_order)

# tulostetaan annetut nimet satunnaisessa järjestyksessä
print("\nTässä kaikki annetut nimet satunnaisessa järjestyksessä:")
for name in input_order:
    print(name)
