class Auto:

    tallissa = 0

    def __init__(self, rekisteritunnus, huippunopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matka = matka
        Auto.tallissa = Auto.tallissa + 1


auto1 = Auto("ABC-123", 142, 0)
print(f"Rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus} km/h.")
