pituus = float(input("Anna mitta tuumina: "))
if pituus < 0:
    print("Negatiivinen mitta. Tack och adjö!")
else:
    tuuma = pituus * 2.54
    print(pituus, "tuumaa on", tuuma, "senttimetriä.")