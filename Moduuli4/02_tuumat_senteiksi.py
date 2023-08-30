length = int(input("Anna mitta sentteinä: "))
if length < 2.54:
    print("Liian lyhyt mitta. Tack och adjö!")
else:
    inch = length / 2.54
    print(length, "senttimetriä on", inch, "tuumaa.")