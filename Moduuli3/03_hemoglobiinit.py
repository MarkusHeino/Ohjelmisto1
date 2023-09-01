gender = input("Anna biologinen sukupuoli (mies tai nainen): ")

hemoglobiini = input("Anna hemoglobiiniarvo grammoina litrassa: ")
isvalid = hemoglobiini.replace(".", "").isnumeric()
if isvalid:
    hemoglobiini = float(hemoglobiini)

    if gender.lower() == "mies":

        if hemoglobiini < 134:
            print(f"Hemoglobiiniarvo {hemoglobiini} on alhainen.")

        elif hemoglobiini > 195:
            print(f"Hemoglobiiniarvo {hemoglobiini} on korkea.")

        elif 134 <= hemoglobiini <= 195:
            print(f"Hemoglobiiniarvo {hemoglobiini} on normaali.")

    if gender.lower() == "nainen":

        if hemoglobiini < 117:
            print(f"Hemoglobiiniarvo {hemoglobiini} on alhainen.")

        elif hemoglobiini > 175:
            print(f"Hemoglobiiniarvo {hemoglobiini} on korkea.")

        elif 117 <= hemoglobiini <= 175:
            print(f"Hemoglobiiniarvo {hemoglobiini} on normaalin rajoissa.")

else:
    print("Väärä arvo.")
