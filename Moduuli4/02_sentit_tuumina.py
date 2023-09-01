length = int(input("Anna mitta tuumina: "))
if length < 0:
    print("Liian lyhyt mitta. Tack och adjö!")
else:
    inch = length * 2.54
    print(length, "tuumaa on", inch, "senttimetriä.")