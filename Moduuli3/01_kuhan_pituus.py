unit = input("Anna kuhan pituus senttimetreinä: ")
isvalid = unit.replace(".", "").isnumeric()
if isvalid:
    unit = float(unit)

    if unit < 37:
        print(f"{unit} on alamittainen. Laske kuha alas! Veteen! Alamitan raja on {37 - unit} cm päässä!")

    elif unit == 37:
        print(f"{unit} on hiinä ja hiinä, mutta hyväksytään!")

    elif unit > 37.1:
        print(f"{unit} on yli sallitun rajan. Kuha kuha on täysmittainen, niin kaikki OK!")

else:
    print("Tämä ei ole järkevä kuhan mitta.")
