isoin = None
pienin = None

while True:
    num = input("Anna luku. Tyhjä lopettaa: ")
    if num == "":
        break
    try:
        num = int(num)
    except:
        print("Virheellinen arvo!")
        continue
    if isoin is None:
        isoin = num
    elif isoin < num:
        isoin = num
    if pienin is None:
        pienin = num
    elif num < pienin:
        pienin = num

print("Isoin numero oli ", isoin)
print("Pienin numero oli", pienin)