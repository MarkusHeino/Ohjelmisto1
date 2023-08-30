try:
    vuosi = int(input("Anna vuosiluku: "))

    if vuosi % 4 == 0:
        print("Vuosiluku {0} on karkausvuosi.".format(vuosi))

    elif (vuosi % 100 != 0) and (vuosi % 400 == 0):
        print("Vuosiluku {0} on karkausvuosi.".format(vuosi))

    else:
        print("Vuosiluku {0} ei ole karkausvuosi.".format(vuosi))

except ValueError:
    print("Tämä ei ole oikea vuosiluku!")
