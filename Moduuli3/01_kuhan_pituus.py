unit = float(input("Anna kuhan pituus senttimetreinä: "))

if unit < 37:
    print(f"{unit} on alamittainen. Laske se kuha alas! Veteen! Alamitan raja on {37 - unit} cm pidempi!")

elif unit == 37:
    print(f"{unit} on hiinä ja hiinä, mutta hyväksytään!")

elif unit > 37.1:
    print(f"{unit} on yli sallitun rajan. Kuha on täysmittainen, niin kaikki OK!")
