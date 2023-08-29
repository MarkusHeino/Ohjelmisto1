

luku = int(input("Paljon rahulia taskussa?"))

if luku > 5:
    print("Enemmän kuin tarpeeksi! Osta latte!")
    luku = luku - 5

print(f"Rahulia ois sen jälkeen: {luku}")


ikä = int(input("Anna ikä:"))

if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))

if ikä >= 18 or ikä >= 15 and paino >= 55:
    print("Lääkkeen käyttö on sallittua!")

else:
    print("Lääkkeen käyttö sallittua!")
