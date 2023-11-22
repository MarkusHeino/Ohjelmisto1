largest = None
smallest = None

while True:
    num = input("Anna luku: ")
    if num == "":
        break
    try:
        num = int(num)
    except:
        print("Virheellinen arvo!")
        continue
    if largest is None:
        largest = num
    elif largest < num:
        largest = num
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Isoin numero oli ", largest)
print("Pienin numero oli", smallest)