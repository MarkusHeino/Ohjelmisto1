

luku = int(input("Paljon rahulia taskussa?"))

if luku > 5:
    print("Enemmän kuin tarpeeksi! Osta latte!")
    luku = luku - 5

print(f"Rahulia ois sen jälkeen: {luku}")


counter = 0
isValue = True
while counter < 5 and isValue:

    ikä = int(input("Anna ikä:"))

    if 15 <= ikä < 18:
        paino = float(input("Anna paino (kg): "))

    if ikä >= 18 or ikä >= 15 and paino >= 55:
        counter += 1
        print("Lääkkeen käyttö on sallittua!")
        isValue = False
    else:
        print("Lääkkeen ei ole sallittua!")
