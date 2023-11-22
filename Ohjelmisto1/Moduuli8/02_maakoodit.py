import mysql.connector
import SQLconfig
def get_airports_by_country(country_code):
    sql = "SELECT ident, airport FROM ident= {country_code}"
    sql += " Country_code ='" + country_code + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


def classify_airports(airports):
    large_airports = []
    small_airports = []
    helicopter_ports = []

    for airport in airports:
        airport_type = airport[2].strip()
        if "iso" in airport_type.lower():
            large_airports.append(airport)
        elif "pieni" in airport_type.lower():
            small_airports.append(airport)
        elif "helikopterikenttä" in airport_type.lower():
            helicopter_ports.append(airport)

    return large_airports, small_airports, helicopter_ports


def main():
    country_code = input("Anna maakoodi (esim. FI): ")
    airports = get_airports_by_country(country_code)

    if airports:
        large_airports, small_airports, helicopter_ports = classify_airports(airports)

        print(f"\nIsoja lentokenttiä {country_code}:")
        for airport in large_airports:
            print(airport[1])

        print(f"\nPieniä lentokenttiä {country_code}:")
        for airport in small_airports:
            print(airport[1])

        print(f"\nHelikopterikenttiä {country_code}:")
        for airport in helicopter_ports:
            print(airport[1])
    else:
        print("Ei löydy tietoja kyseisellä koodilla..")

