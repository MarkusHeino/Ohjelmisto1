class Auto:

    tallissa = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
        Auto.tallissa = Auto.tallissa + 1

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos

        if self.nopeus < self.huippunopeus:

            if self.nopeus < 0:
                self.nopeus = 0
                return


auto1 = Auto("ABC-123", 142, 0)
print(f"Rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus} km/h."
      f"Tämän hetkinen nopeus: {auto1.nopeus} km/h"
      f"Kuljettu matka: {auto1.matka} km.")

# kiihdyttäminen vaiheittain 30, 70 ja 50 km/h
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton nopeus kiihdyttämisen jälkeen: {auto1.nopeus} km/h,")

# jarrutetaan
auto1.kiihdyta(-200)

print(f"Auton nopeus jarrutuksen jälkeen: {auto1.nopeus} km/h.")
