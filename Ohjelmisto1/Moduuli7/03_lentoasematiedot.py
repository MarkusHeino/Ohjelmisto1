# luodaan tyhjä tietokanta lentokenttätiedoille
airport_data = {}

# luodaan funktio hakemaan lentokentän tiedot tietokannasta
def fetch_airport_info(icao_code):
    if icao_code in airport_data:
        return airport_data[icao_code]
    else:
        return None

# luodaan looppaava kysely tietojen antoa, hakua ja lopettamista varten
while True:
    print("\nTervetuloa lentokenttätietokantaan!")
    print("1. Anna uusi lentokenttä ja ICAO-koodi: ")
    print("2. Hae lentokentän nimi ja ICAO-koodi: ")
    print("3. Lopeta ohjelma")

    choice = input("Valitse (1/2/3): ")

    if choice == "1":
        icao_code = input("Anna lentokentän ICAO-koodi: ").strip().upper()
        airport_name = input("Anna lentokentän nimi: ")
        airport_data[icao_code] = airport_name
        print(f"Lisättiin {icao_code}: {airport_name} tietokantaan.")

    # kysytään ICAO-koodilla - haku ei onnistu tällä tavoin sekä koodilla että nimellä... tarvitaan lisätietokanta ja muokattu hakufunktio
    elif choice == "2":
        search_query = input("Anna lentokentän ICAO-koodi: ").strip().upper()
        airport_info = fetch_airport_info(search_query)

        if airport_info:
            print(f"ICAO-koodi: {search_query}, lentokentän nimi: {airport_info}")
        else:
            print("Lentokenttää ei löydy vielä tietokannasta. Valitse 1 lisätäksesi se.")

    elif choice == "3":
        break

    else:
        print("Väärä valinta. Valitse ystävällisesti 1, 2 tai 3.")

print("Ohjelma suljettu.")
