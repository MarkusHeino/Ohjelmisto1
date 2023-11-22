import random

class Auto:
    def __init__(self, reg_number, top_speed):
        self.reg_number = reg_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self):
        self.current_speed = random.randint(0, self.top_speed)

    def travel_one_hour(self):
        self.accelerate()
        self.distance_traveled += self.current_speed

class Sähköauto(Auto):
    def __init__(self, reg_number, top_speed, battery_capacity):
        super().__init__(reg_number, top_speed)
        self.battery_capacity = battery_capacity

    def travel_one_hour(self):
        super().travel_one_hour()
        battery_consumption = random.uniform(5, 8)  # satunnainen sähkönkulutus nopeuden mukaan
        self.battery_capacity -= battery_consumption

class Polttomoottoriauto(Auto):
    def __init__(self, reg_number, top_speed, gas_tank_capacity):
        super().__init__(reg_number, top_speed)
        self.gas_tank_capacity = gas_tank_capacity

    def travel_one_hour(self):
        super().travel_one_hour()
        fuel_consumption = random.uniform(6, 10)  # satunnainen bensankulutus nopeuden mukaan
        self.gas_tank_capacity -= fuel_consumption

# luodaan sähköautomalli ja polttomoottoriversio
electric_car = Sähköauto("ABC-15", 180, 52.5)
combustion_engine_car = Polttomoottoriauto("ACD-123", 165, 32.3)

# simuloidaan kisa kolmen tunnin pituiseksi
for hour in range(1, 4):
    print(f"Hour {hour}:")

    electric_car.travel_one_hour()
    combustion_engine_car.travel_one_hour()

    print(f"Electric Car: Speed - {electric_car.current_speed} km/h, Distance - {electric_car.distance_traveled} km, Battery - {electric_car.battery_capacity} kWh")
    print(f"Combustion Engine Car: Speed - {combustion_engine_car.current_speed} km/h, Distance - {combustion_engine_car.distance_traveled} km, Fuel - {combustion_engine_car.gas_tank_capacity} liters")

# kerrotaan voittaja kolmen tunnin kisailun päätteeksi -- Lisäsin mukaan vielä tiedot kulutetusta akkuvirrasta ja polttoaineesta. ..koska muutenhan ominaisuuksilla ei tee mitään?
if electric_car.distance_traveled > combustion_engine_car.distance_traveled:
    print("Electric Car traveled farther.")
elif electric_car.distance_traveled < combustion_engine_car.distance_traveled:
    print("Combustion Engine Car traveled farther.")
else:
    print("Both cars traveled the same distance.")

print(f"Electric Car Battery Remaining: {electric_car.battery_capacity} kWh")
print(f"Combustion Engine Car Fuel Remaining: {combustion_engine_car.gas_tank_capacity} liters")
