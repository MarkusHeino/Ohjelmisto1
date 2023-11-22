import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        lisa_matka = self.nopeus * aika
        self.matka += lisa_matka

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        sorted_cars = sorted(self.autot, key=lambda x: x.matka, reverse=True)
        print("Car\t\tMax Speed    \tEnd Speed    \tDistance")
        for auto in sorted_cars:
            print(f"{auto.rekisteritunnus:6s}\t{auto.huippunopeus:3d} km/h\t\t{auto.nopeus:3d} km/h\t\t{auto.matka:3d} km.")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

# luodaan kilpailu Suuri romuralli kymmenelle autolle
autot = [Auto(f"ABC-{nro}", random.randint(100, 200)) for nro in range(1, 11)]
race = Kilpailu("Suuri romuralli", 8000, autot)

time = 0
print("Kilpailu alkaa!")

while not race.kilpailu_ohi():
    race.tunti_kuluu()
    time += 1

    # tulosta tilannetietoja 10 tunnin välein
    if time % 10 == 0:
        race.tulosta_tilanne()

# tulostetaan lopullinen tilanne kun voittaja on selvinnyt
race.tulosta_tilanne()
print(f"Kilpailun kesto oli {time} tuntia.")
print("Kilpailu on päättynyt!")

