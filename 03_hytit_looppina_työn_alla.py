value = int(input("Anna hyttiluokkasi tunnus: LUX, A, B tai C: "))

while value == "A":
    print(f"A on ikkunallinen hytti autokannen yläpuolella.")
    break
while value == "B":
    print(f"B on ikkunaton hytti autokannen yläpuolella.")
    break
while value == "C":
    print(f"C on ikkunaton hytti autokannen alapuolella.")
    break
while value == "LUX":
    print(f"LUX on parvekkeellinen hytti yläkannella.")
    break
else:
    print("Virheellinen hyttiluokka!")
