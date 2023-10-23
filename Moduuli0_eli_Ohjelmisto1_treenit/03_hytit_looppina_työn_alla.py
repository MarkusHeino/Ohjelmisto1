counter = 0
isValue = True
while counter < 5 and isValue:
    value = input("Anna hyttiluokkasi tunnus: LUX, A, B tai C: ")
    counter += 1
    if value == "A":
        print(f"A on ikkunallinen hytti autokannen yläpuolella.")
        isValue = False

    elif value == "B":
        print(f"B on ikkunaton hytti autokannen yläpuolella.")
        isValue = False

    elif value == "C":
        print(f"C on ikkunaton hytti autokannen alapuolella.")
        isValue = False

    elif value == "LUX":
        print(f"LUX on parvekkeellinen hytti yläkannella.")
        isValue = False

    else:
        print("Virheellinen hyttiluokka!")
