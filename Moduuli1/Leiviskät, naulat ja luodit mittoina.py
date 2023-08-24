a = int(input("Lasketaan massa! Anna leiviskät:"))
b = int(input("Sitten anna naulat:"))
c = int(input("Ja vielä luodit:"))

gram = (a*8512+b*425.6+c*13.3)
kg = int(gram / 1000)
remainder_gram = gram % 1000

print (f"Massa on nykymittojen mukaan",(kg), "kilogrammmaa ja", "%0.2f" % remainder_gram, "grammaa.")
