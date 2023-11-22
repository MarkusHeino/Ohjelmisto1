from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    geolocator = Nominatim(user_agent="lentokenttien etäisyys")
    location = geolocator.geocode(icao_code)
    if location:
        return (location.latitude, location.longitude)
    else:
        print(f"Ei löydy koordinaatteja {icao_code}.")
        return None

def calculate_distance_between_airports(icao_code1, icao_code2):
    coordinates1 = get_airport_coordinates(icao_code1)
    coordinates2 = get_airport_coordinates(icao_code2)

    if coordinates1 and coordinates2:
        distance = geodesic(coordinates1, coordinates2).kilometers
        return distance
    else:
        return None


icao_code1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").upper()
icao_code2 = input("Anna toisen lentokentän ICAO-kood: ").upper()

distance = calculate_distance_between_airports(icao_code1, icao_code2)

if distance is not None:
    print(f" {icao_code1} ja {icao_code2} välinen etäisyys on {distance:.2f} kilometriä.")
else:
    print("Ei voida laskea etäisyyttä. Anna ICAO-koodit uudelleen.")
