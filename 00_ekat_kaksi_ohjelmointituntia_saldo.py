
käyttäjä = input("Markus Heino:")
print("Hauska tavata," +käyttäjä + "!")

käyttäjä = " Elvis"
print("Hauska tavata," +käyttäjä + "!")

grammat = float(input("Anna grammat"))

grammat = 123456
kg = int(grammat / 1000)
jäännös_grammat = grammat % 1000

print(kg, jäännös_grammat, sep=';')
print(jäännös_grammat)

print(f'Kilot on: {kg-jäännös_grammat:6.1f}')



a = int(input("Lasketaan massa! Anna leiviskät: "))
b = int(input("Anna naulat: "))
c = int(input("Anna luodit: "))

a = 8512 * gram
b = 425,6 * gram
c = 13,3 * gram

kg = (a + b + c)/1000
remainder_gram = int(gram % 1000)

print("Massa on:"(kg) + "ja" + (remainder_gram) + "grammaa.")
