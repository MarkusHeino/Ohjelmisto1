gender = input("Anna biologinen sukupuoli: ")

hemoglobiini = input("Anna hemoglobiiniarvosi (g/l): ")
hemoglobiini = int(hemoglobiini)

if gender == "Nainen" or "nainen" in gender:

    if hemoglobiini < 117:
        print(f"Hemoglobiiniarvosi {hemoglobiini} on alhainen.")

    elif hemoglobiini > 175:
        print(f"Hemoglobiiniarvosi {hemoglobiini} on korkea")

    elif 117 >= hemoglobiini <= 175:
        print(f"Hemoglobiinisi {hemoglobiini} on OK")

if gender == "Mies" or "mies" in gender:

    if hemoglobiini < 134:
        print(f"Hemoglobiiniarvosi {hemoglobiini} on alhainen.")

    elif hemoglobiini > 195:
        print(f"Hemoglobiiniarvosi {hemoglobiini} on korkea")

    elif 134 <= hemoglobiini <= 195:
        print(f"Hemoglobiinisi {hemoglobiini} on OK")
