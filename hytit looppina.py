while True:

    value = input("Anna hyttiluokkasi tunnus: LUX, A, B tai C: ")

    for retry in range(5):

        if value == "A":
            print(f"A on ikkunallinen hytti autokannen yläpuolella.")

        elif value == "B":
            print(f"B on ikkunaton hytti autokannen yläpuolella.")

        elif value == "C":
            print(f"C on ikkunaton hytti autokannen alapuolella.")

        elif value == "LUX":
            print(f"LUX on parvekkeellinen hytti yläkannella.")

        else:
            print("Virheellinen hyttiluokka!")


