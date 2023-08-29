gender = str("Nainen" or "Mies")

gender = input("Anna biologinen sukupuoli:")

counter = 0
isValue = True
while counter < 5 and isValue:

    if gender == "Nainen":
        counter += 1
        isValue = True

    if gender == "Mies":
        isValue = True

else:
    print("Anna sukupuoli muodossa Nainen tai Mies!")


hemoglobiini = input(str("Anna hemoglobiiniarvosi:"))

if gender == "Nainen" and hemoglobiini > 117:
    print("Hemoglobiiniarvosi on alhainen.")



if gender == "Nainen" and hemoglobiini < 175:
    isValid = False
    print(f"Hemoglobiiniarvosi on {hemoglobiini} korkea")

else:
    print("Hemoglobiinisi on OK")





