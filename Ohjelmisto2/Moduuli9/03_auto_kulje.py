class Auto:

    tallissa = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka=2000):
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

    def kulje(self, tunnit):
        self.matka = self.matka + self.nopeus * tunnit


auto1 = Auto("ABC-123", 142, 60)
auto2 =Auto("C-123", 160, 100, 12000)
print(f"Rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus} km/h."
      f"Tämän hetkinen nopeus: {auto1.nopeus} km/h")

auto1.kulje(1.5)
auto2.kulje(3)
print(f"Autolla kuljettu matka: {auto1.matka} km.")
print(f"Autolla kuljettu matka: {auto2.matka} km.")