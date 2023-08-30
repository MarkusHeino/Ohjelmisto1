gender = str(input("Anna biologinen sukupuoli: "))

hemoglobiini = int(input("Anna hemoglobiiniarvo grammoina litrassa: "))

if gender == "Nainen" and hemoglobiini < 117:
    print(f"Hemoglobiiniarvo {hemoglobiini} on alhainen.")

elif gender == "Nainen" and hemoglobiini > 175:
    print(f"Hemoglobiiniarvo {hemoglobiini} on korkea.")

elif gender == "Nainen" and 117 <= hemoglobiini <= 175:
    print(f"Hemoglobiiniarvo {hemoglobiini} on normaalin rajoissa.")

if gender == "Mies" and hemoglobiini < 134:
    print(f"Hemoglobiiniarvo {hemoglobiini} on alhainen.")

elif gender == "Mies" and hemoglobiini > 195:
    print(f"Hemoglobiiniarvo {hemoglobiini} on korkea.")

elif gender == "Mies" and 134 <= hemoglobiini <= 195:
    print(f"Hemoglobiiniarvo {hemoglobiini} on normaali.")
