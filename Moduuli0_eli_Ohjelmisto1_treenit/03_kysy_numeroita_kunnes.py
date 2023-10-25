isoin = None
pienin = None

while True:
    try:
        numero = input("Anna luku: ")
        if numero == "":
            break
        try:
            num = int(num)
        except:
            print("Virheellinen valinta.")
            continue
        numero = str(numero)
        isoin = numero if isoin < numero or isoin == None else pienin
        pienin = numero if pienin > numero or pienin == None else pienin

    finally:
        print("Isoin luku oli ", isoin)
        print("Pienin luku oli ", pienin)
