a = int(input("Lasketaan massa! Anna leiviskät: "))
b = int(input("Anna naulat: "))
c = int(input("Anna luodit: "))

gram = 13,3 * c
kilogram = (1000 * gram)

a = 8512 * gram
b = 425,6 * gram
c = 13,3 * gram

print("Massa nykymittojen mukaan:", kilogram, "kilogrammaa ja", gram, "grammaa.")

print(f"Massa nykymittojen mukaan: {kilogram:2.0f}", "kilogrammaa ja , {gram:3.2f}","grammaa.")