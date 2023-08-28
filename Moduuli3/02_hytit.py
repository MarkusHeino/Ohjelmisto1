unit = float(input("Anna hyttiluokkasi tunnus: LUX, A, B tai C: "))

if unit == A:
    print(f"{unit} on ikkunallinen hytti autokannen yläpuolella.")

elif unit == B:
    print(f"{unit} on ikkunaton hytti autokannen yläpuolella.")

elif unit == C:
    print(f"{unit} on ikkunaton hytti autokannen alapuolella.")

elif unit == LUX:
    print(f"{unit} on parvekkeellinen hytti yläkannella.")

else:
    print("Kyseistä hyttiluokkaa ei ole. Anna hyttiluokkasi tunnuksena joko LUX, A. B tai C! "))