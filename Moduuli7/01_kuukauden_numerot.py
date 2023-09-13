seasons = (1.0, 2.0, 3.0, 4.0)

try:
    month_number = int(input("Anna kuukauden numero väliltä 1-12: "))

    if month_number < 1 or month_number > 12:
        print("Ei kuulu vaihtoehtoihin. Anna numero väliltä 1-12.")
    else:

        season_index = (month_number % 12) // 3
        season = seasons[season_index]

        if season == 1.0:
            print("Kuukauden vuodenaika on talvi.")
        elif season == 2.0:
            print("Kuukauden vuodenaika on kevät.")
        elif season == 3.0:
            print("Kuukauden vuodenaika on kesä.")
        else:
            print("Kuukauden vuodenaika on syksy.")

except ValueError:

    print("Väärä arvo. Anna kuukauden numero muodossa 1-12.")
