count = 0
while True:
    userName = input("Anna käyttäjätunnus: ")
    password = input("Salasana: ")
    count += 1
    if count == 5:
        print("Pääsy evätty.")
        break  # exit

    elif userName == 'python' and password == 'rules':
        print("Tervetuloa!")
        break

    else:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen!")

