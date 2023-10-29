import random

class Car:
    def __init__(self, number):
        self.rekisteritunnus = f"ABC-{number}"
        self.huippunopeus = random.randint(100, 200)
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self):
        muutos = random.randint(-10, 15)
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self):
        self.matka += self.nopeus


def main_program():
    autot = [Car(i) for i in range(1, 11)]

    for car in autot:
        car.kiihdyta()

    time = 0
    winner = None

    while not winner:
        for car in autot:
            car.kiihdyta()
            car.kulje()
            if car.matka >= 10000:
                winner = car
                break
        time += 1

    autot.sort(key=lambda car: car.matka, reverse=True)

    print("Car\t\tMax Speed    \tEnd Spd     \tDistance")
    for car in autot:
        print(f"{car.rekisteritunnus:6s}\t{car.huippunopeus:3d} km/h\t\t{car.nopeus:3d} km/h\t\t{car.matka:3d} km.")

    print(f"Kilpailun kesto oli {time} tuntia.")


if __name__ == "__main__":
    main_program()
