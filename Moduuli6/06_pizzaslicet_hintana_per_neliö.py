import math

def calculate_unit_price(diameter_cm, price):
    diameter_m = diameter_cm / 100.0

    area_m2 = math.pi * (diameter_m / 2) ** 2

    unit_price = price / area_m2

    return unit_price

diameter1_cm = float(input("Anna pizzan nro. 1 halkaisija senttimetreinä: "))
price1 = float(input("Ja hinta euroina: "))

diameter2_cm = float(input("Anna pizzan nro. 2 halkaisija senttimetreinä: "))
price2 = float(input("Ja vielä senkin hinta euroina: "))

unit_price1 = calculate_unit_price(diameter1_cm, price1)

unit_price2 = calculate_unit_price(diameter2_cm, price2)

if unit_price1 < unit_price2:
    print("\nPizza nro. 1 on parempi diili. Enemmän pizzaa per euro.")
elif unit_price2 < unit_price1:
    print("\nPizza nro. 2 on parempi diili. Enemmän pizzaa per euro.")
else:
    print("\nMolemmat pizzat ovat yhtä hyviä pizza per euro -skaalassa. Molempi parempi.")
