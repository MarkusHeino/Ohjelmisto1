def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

while True:
    gallons = float(input("Anna gallonoiden määrä. Negatiivinen luku lopettaa ohjelman: "))

    if gallons < 0:
        break

    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallonaa on yhtä kuin {liters} litraa.")
